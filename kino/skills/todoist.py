
import arrow
from dateutil.parser import parse
import re
from pytz import timezone
import todoist

from ..slack.resource import MsgResource
from ..slack.slackbot import SlackerAdapter
from ..slack.template import MsgTemplate

from ..utils.config import Config
from ..utils.profile import Profile


class TodoistManager(object):

    def __init__(self, text=None):
        self.input = text
        self.config = Config()
        self.todoist_api = todoist.TodoistAPI(
            self.config.open_api['todoist']['TOKEN'])

        self.slackbot = SlackerAdapter()
        self.template = MsgTemplate()

    def schedule(self, channel=None):
        self.slackbot.send_message(text=MsgResource.TODOIST_TODAY_SCHEDULE)

        overdue_task_count = self.__get_overdue_task(kind="count")
        today_task = self.__get_today_task()
        today_task_count = len(today_task)

        task_text = MsgResource.TODOIST_OVERDUE(
            overdue_task_count) + "\n" + MsgResource.TODOIST_TODAY(today_task_count)
        self.slackbot.send_message(text=task_text, channel=channel)

        specific_task_list = list(
            filter(
                lambda x: x[2] != "anytime",
                self.__get_task(today_task)))
        attachments = self.template.make_todoist_task_template(
            specific_task_list)
        self.slackbot.send_message(attachments=attachments, channel=channel)

        karma_trend = self.__get_karma_trend()
        karma_trend_text = MsgResource.TODOIST_KARMA(karma_trend)
        self.slackbot.send_message(text=karma_trend_text, channel=channel)

    def __get_overdue_task(self, kind="count"):
        task_list = []
        # 7 day ~ 1 day before
        for i in range(7, 0, -1):
            query = str(i) + ' day before'
            before = self.todoist_api.query([query])[0]['data']
            task_list += before

        if kind == "all":
            return task_list
        elif kind == "count":
            return len(task_list)
        elif kind == "point":
            return self.__get_point(task_list)

    def __get_point(self, task_list):
        point = 0
        for task in task_list:
            point += (task['priority'] + 1)
        return point

    def __get_today_task(self):
        self.todoist_api.sync()
        return self.todoist_api.query(['today'])[0]['data']

    def get_repeat_task_count(self):
        task = self.__get_today_task()
        task = list(filter(lambda t: '분' in t['content'], task))
        return len(task)

    def remain_task(self):
        today_task = self.__get_today_task()
        remain_task_list = self.__get_task(today_task)

        remain_task_count = len(remain_task_list)
        if remain_task_count > 0:
            self.slackbot.send_message(text=MsgResource.TODOIST_REMAIN)
        self.slackbot.send_message(
            text=MsgResource.TODOIST_FEEDBACK_OVERDUE(remain_task_count))

        attachments = self.template.make_todoist_task_template(
            remain_task_list)
        self.slackbot.send_message(attachments=attachments)

    def __get_task(self, today_task):
        task_list = []
        for t in today_task:
            due_time = "anytime"
            if ':' in t['date_string'] or '분' in t['date_string']:
                due_time = parse(
                    t['due_date']).astimezone(
                    timezone('Asia/Seoul'))
                due_time = due_time.strftime("%H:%M")

            project = self.todoist_api.projects.get_data(t['project_id'])
            project_name = project['project']['name']

            task_list.append(
                (project_name, t['content'], due_time, t['priority']))
        return task_list

    def __get_karma_trend(self):
        user = self.todoist_api.user.login(
            self.config.open_api['todoist']['ID'],
            self.config.open_api['todoist']['PASSWORD'])
        return user['karma_trend']

    def feedback(self, channel=None):
        self.slackbot.send_message(text=MsgResource.TODOIST_FEEDBACK)

        overdue_task_count = self.__get_overdue_task(kind="count")
        today_task = self.__get_today_task()
        today_task_count = len(today_task)

        overdue_today_text = MsgResource.TODOIST_FEEDBACK_OVERDUE(
            overdue_task_count + today_task_count)
        self.slackbot.send_message(text=overdue_today_text, channel=channel)

        added_count, completed_count, updated_count = self.__get_event_counts()
        event_text = MsgResource.TODOIST_FEEDBACK_EVENT(
            added_count, completed_count, updated_count)
        self.slackbot.send_message(text=event_text, channel=channel)

    def __get_event_counts(self):
        activity_log_list = self.todoist_api.activity.get()
        added_task_count = 0
        completed_task_count = 0
        updated_task_count = 0

        today = arrow.now().to('Asia/Seoul')
        start, end = today.span('day')

        for log in activity_log_list:
            event_date = arrow.get(
                log['event_date'],
                'DD MMM YYYY HH:mm:ss Z').to('Asia/Seoul')
            if event_date < start or event_date > end:
                continue

            event_type = log['event_type']
            if event_type == 'added':
                added_task_count += 1
            elif event_type == 'completed':
                completed_task_count += 1
            elif event_type == 'updated':
                updated_task_count += 1
        return added_task_count, completed_task_count, updated_task_count

    def __parse_assigned_time(self, content):
        min_re = "\d+분"
        assigned_time = re.search(min_re, content)
        if assigned_time is not None:
            return int(assigned_time.group()[:-1])
        else:
            return None

    def complete_by_toggl(self, description, time):
        description = description.strip()
        is_contain_item = False

        task, assigned_time = self.__get_task_by_name(description)
        if task is None:
            print('todoist에 관련된 일이 없습니다.')
        else:
            self.__complete(task, assigned_time=assigned_time, time=time)

    def __get_task_by_name(self, name):
        name = name.split(" - ")[0]

        tasks = self.__get_today_task()
        for t in tasks:
            content = t['content']
            if name in content:
                assigned_time = self.__parse_assigned_time(content)
                return t, assigned_time
        return None, None

    def __complete(self, task, assigned_time=None, time=None):
        item = self.todoist_api.items.get_by_id(task['id'])
        if (assigned_time is None) or (time >= assigned_time):
            self.__update_task_duration(item, task, assigned_time)
            if "매" in task['date_string']:
                self.todoist_api.items.update_date_complete(
                    task['id'], date_string=task['date_string'])
            else:
                item.complete()
        else:
            content = task['content'].replace(
                str(assigned_time), str(assigned_time - time))
            item.update(content=content)
        self.todoist_api.commit()

    def __update_task_duration(self, item, task, assigned_time):
        if assigned_time is None:
            return

        profile = Profile()
        if "매일" in task['date_string']:
            task_duration = profile.get_task('EVERY_DAY_DURATION')
        elif "평일" in task['date_string']:
            task_duration = profile.get_task('EVERY_WEEKDAY_DURATION')
        else:
            task_duration = profile.get_task('SOME_WEEKDAY_DURATION')
        content = task['content'].replace(
            str(assigned_time), str(task_duration))
        item.update(content=content)

    def get_point(self):
        overdue_task_point = self.__get_overdue_task(kind="point")
        today_task_point = self.__get_point(self.__get_today_task())

        max_point = 100
        total_minus_point = overdue_task_point + today_task_point
        if total_minus_point > max_point:
            total_minus_point = max_point
        return max_point - total_minus_point

    def auto_update_tasks(self):
        overdue_task_list = self.__get_overdue_task(kind="all")
        today_format = arrow.now().format("YYYY-M-DDT00:00")
        for task in overdue_task_list:
            item = self.todoist_api.items.get_by_id(task['id'])
            assigned_time = self.__parse_assigned_time(task['content'])
            self.__update_task_duration(item, task, assigned_time)
            self.todoist_api.items.update_date_complete(
                task['id'], date_string=task['date_string'],
                new_date_utc=today_format, is_forward=0)
        self.todoist_api.commit()
        self.slackbot.send_message(text=MsgResource.TODOIST_AUTO_UPDATE)
