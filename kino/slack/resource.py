class MsgResource:

    def HELLO(master_name, bot_name):
        return f"{master_name}님 안녕하세요! \n저는 개인비서 {bot_name} 라고 합니다.\n반갑습니다."

    ERROR = "에러가 발생하였습니다."
    NOT_UNDERSTANDING = "무슨 말인지 잘 모르겠어요. 저를 똑똑하게 만들어주세요!!"
    CREATE = "등록이 완료되었습니다!"
    EMPTY = "비어있습니다. 새로 등록해주세요!."
    READ = "등록된 리스트입니다."
    UPDATE = "변경이 완료되었습니다."
    DELETE = "삭제 완료!"

    NAP = "헛.. 죄송합니다. 제가 잠시 졸고 있었습니다ㅠㅠ"

    WORKER_START = "넵, 일 열심히 하겠습니다ㅎㅎ"
    WORKER_STOP = "휴.. 드디어 휴식시간이군요!\n필요하실 때 언제나 불러주세요ㅎㅎ"

    WORKER_CREATE_START = "요청하신 일을 만들도록 하겠습니다!"
    WORKER_FUNCTION_NOT_FOUND = "어떤 기능을 원하시는 것인지 잘 모르겠어요ㅠㅠ 조금 더 정확하게 말씀해주세요."

    GUIDE = "Kino에 대한 간략한 소개 및 도움말 입니다."
    GREETING = "저를 찾으셨나요! 무엇을 도와드릴까요?"

    SCHEDULER_CREATE_START = "알람 등록을 진행합니다."
    SCHEDULER_CREATE_STEP1 = "반복 알람을 사용할 경우는 시간대를 선택 하시고,\n 한 번 알리는 경우 새로운 시간을 입력해주세요!\n (ex. #1 or 10:00)"
    SCHEDULER_CREATE_STEP1_ONLY_TIME = "시간을 입력해주세요!\n (ex. 10:00)"
    SCHEDULER_CREATE_STEP2 = "다음으로 주기를 입력해주세요!\n (ex. 30 분)"
    SCHEDULER_CREATE_STEP3 = "사용될 함수는 무엇인가요?\n (ex. send_message, {\"text\"=\"Test!\"})"

    SCHEDULER_DELETE_START = "알람 삭제를 진행합니다.\n지우고자 하시는 알람의 인덱스를 입력해주세요!"

    BETWEEN_CREATE_START = "시간대 등록을 진행합니다."
    BETWEEN_CREATE_STEP1 = "시간간격을 입력해주세요!\n(ex. 12:00~19:00)"
    BETWEEN_CREATE_STEP2 = "입력하신 시간대를 설명해주시겠어요?\n (ex. 업무 시간)"

    BETWEEN_DELETE_START = "시간대 삭제를 진행합니다.\n지우고자 하시는 시간대의 인덱스를 입력해주세요!"

    GITHUB_COMMIT_EMPTY = "Github에 Commit한 기록이 없습니다. 일일커밋 실천하셔야죠!"
    GITHUB_COMMIT_EXIST = "오, Commit을 하셨군요! 멋지십니다.ㅎㅎ 오늘 하루 Commit 수 : "
    GITHUB_COMMIT_WEEKLY = "일주일간의 Github commit 을 확인하세요!"

    ROBOT_ICON = ":robot_face: "
    TIMER_ICON = ":mantelpiece_clock: "
    CLOCK_ICON = ":alarm_clock: "
    WHITE_LIST_ICON = ":white_medium_small_square: "
    WHITE_ELEMENT_ICON = "   :white_circle: "
    BLACK_LIST_ICON = ":black_medium_small_square: "
    BLACK_ELEMENT_ICON = "   :black_circle: "
    BLUE_DIAMOND_ICON = ":small_blue_diamond: "
    ORANGE_DIAMOND_ICON = ":small_orange_diamond: "
    SEND_MESSAGE_ICON = ":speech_balloon: "
    DAILY_COMMIT_ICON = ":octocat: "

    PROFILE_WAKE_UP = ":bell: 이제 일어날 시간 입니다! :bell: "
    PROFILE_WORK_START = "오늘 하루도 화이팅입니다!ㅎㅎ :raised_hands:"
    PROFILE_WORK_END = "고생하셨습니다! 푹 쉬시면서, 자기발전도 하시고 알찬 저녁 보내세요. :night_with_stars:"
    PROFILE_GO_TO_BED = ":sleeping_accommodation: 이제 주무실 시간입니다! "

    WEATHER = "날씨 정보를 알려드립니다."
    WEATHER_ICON = ":full_moon_with_face: "
    WEATHER_ICONS = {
        "clear-day": ":sunny: ",
        "clear-night": ":first_quarter_moon_with_face: ",
        "rain": ":umbrella_with_rain_drops: ",
        "snow": ":snowman: ",
        "sleet": ":snow_cloud: ",
        "wind": ":wind_blowing_face: ",
        "fog": ":fog: ",
        "cloudy": ":cloud: ",
        "partly-cloudy-day": ":partly_sunny: ",
        "partly-cloudy-night": ":night_with_stars: "
    }

    YOUTUBE_DOWNLOADER = "요청하신 YouTube 다운로드 링크입니다."
    YOUTUBE_ICON = ":video_camera: "

    TODOIST_ICON = ":memo: "
    TODOIST_TODAY_SCHEDULE = "오늘의 스케쥴을 알려드리겠습니다."

    def TODOIST_OVERDUE(task_count):
        return f"기한이 지난 일이 {task_count}개 있습니다."

    def TODOIST_TODAY(task_count):
        return f"오늘 할일의 수는 {task_count}개 입니다."

    def TODOIST_KARMA(trend):
        karma_trend_text = {
            "up": "최근 생산성이 올랐습니다. 이대로 쭉 갑시다!ㅎㅎ",
            "-": "생산성에 변화가 없습니다! 분발하시죠!",
            "down": "최근 생산성이 떨어지고 있습니다. 할일목록을 잘 관리해주세요! ㅠㅠ"
        }
        return karma_trend_text[trend]

    def TODOIST_PRIORITY_COLOR(priority):
        priority_color = {
            1: '#CACACA',
            2: '#FBC03F',
            3: '#F6802E',
            4: '#E24439'
        }
        return priority_color[priority]
    TODOIST_TIME = "에 예정되어 있습니다."
    TODOIST_FEEDBACK = "오늘 Todoist 작업내역 입니다."

    def TODOIST_FEEDBACK_OVERDUE(task_count):
        if task_count > 5:
            return f"아직 처리해야할 일들이 {task_count}개나 남았습니다. ㅠㅠ"
        elif task_count > 0:
            return f"처리해야할 일들이 {task_count}개 남았습니다. 조금만 힘내시죠ㅎㅎ"
        else:
            return "오.. 예정되었던 일들을 전부 처리하셨군요! 이제 푹 쉬세요. :+1: "

    def TODOIST_FEEDBACK_EVENT(a_count, c_count, u_count):
        return f"오늘은 총 {a_count} 개의 할일들을 추가하였고, {c_count} 개의 일들을 완료하였으며, {u_count} 개의 일들을 완료하지 못하고 연기하였습니다."

    TODOIST_REMAIN = "아직 남아있는 작업 리스트입니다. "
    TODOIST_AUTO_UPDATE = "기한이 지난 작업들을 제가 오늘로 업데이트 하였습니다. "

    MAXIM_ICON = ":scales: "

    TOGGL_START = "Toggl을 시작합니다."
    TOGGL_STOP = "Toggl을 중지합니다."

    def TOGGL_STOP_SUMMARY(description, diff_min):
        return description + f" 작업을 {diff_min}분 동안 진행하셨습니다."
    TOGGL_DO_NOTHING = "지금은 아무런 작업도 하고 있지 않으십니다."

    def TOGGL_TIMER_CHECK(minute):
        return f"작업을 진행하신지 {minute}분 경과하였습니다."

    TOGGL_NOTI_RELAY = "작업을 너무 오래하고 계십니다! 잠시 멈추고 십분만 휴식하시죠!!"
    TOGGL_REPORT = "Toggl에 저장되어있는 Report 입니다."
    def TOGGL_ADVICE_REST(time):
        return f"{time} 까지는 쉬는 시간입니다! :dancer:"

    ATTENTION_QUESTION_STEP_0 = "현재 작업에 대해서 얼마나 집중하고 계신가요? (100점 만점)"

    def ATTENTION_QUESTION_STEP_1(happy):
        happy = int(happy)
        if happy >= 92:
            return "몰입력 최고군요! :laughing: "
        elif happy >= 85:
            return "일이 재미있으시군요! ㅎㅎ :smile: "
        elif happy >= 77:
            return "할만한 일인 것 같아요! :smiley: "
        elif happy >= 70:
            return "좀 어렵거나, 재미없으신 일인 것 같군요..! :simple_smile: "
        else:
            return "하기 싫은 작업을 하시는 중이셨군요..ㅠㅠ :angry: "
    ATTENTION_REPORT = "집중도 Report 입니다."

    HAPPY_QUESTION_STEP_0 = "오늘 하루는 어떠셨나요? (100점 만점)"

    def HAPPY_QUESTION_STEP_1(happy):
        happy = int(happy)
        if happy >= 100:
            return "기분 최고!! :laughing: "
        elif happy >= 90:
            return "행복하시군요ㅎㅎ 보기 좋습니다. :smile: "
        elif happy >= 80:
            return "슬며시 미소를 짓고 계신 것 같아요ㅎㅎ :smiley: "
        elif happy >= 70:
            return "그냥 그런 하루 였군요.. :simple_smile: "
        else:
            return "무슨 일 있으신가요? 기분이 안 좋아보입니다ㅠㅠ :angry: "
    HAPPY_REPORT = "행복도 Report 입니다."

    RESCUETIME_EFFICIENCY = "RescueTime 생산성 차트입니다."

    TODAY_BREIFING = "오늘 하루 브리핑을 시작하겠습니다!"
    TODAY_SUMMARY = "오늘 하루 요약을 시작하겠습니다!"

    TOTAL_REPORT = "종합점수 Report 입니다."

    BUS_ICON = ":bus: "

    def SCORE_COLOR(score):
        if score >= 90:
            return "#438C56"
        elif score >= 75:
            return "#38ACEC"
        elif score >= 60:
            return "#FF8040"
        else:
            return "#C11B17"

    APPLAUD = ":clap::clap::clap: 멋지십니다!ㅎㅎ"
    WEEKDAY = "오늘은 평일이군요! 달리시죠ㅎㅎ :running: "
    HOLIDAY = "오늘은 쉬는 날 이군요! 쉬면서 가세요ㅎㅎ :walking: "
    GOOD_MORNING = "안녕히 주무셨나요? 좋은 아침입니다^^ :sun_with_face:"

    def SLEEP_TIME(bed_time, wakeup_time, diff):
        return f"{bed_time} ~ {wakeup_time}, 총 {diff}h 동안 잠을 주무셨습니다."

    GOOD_NIGHT = "이제 주무시는 군요. 좋은 꿈 꾸세요 :first_quarter_moon_with_face:"

    def AIR_QUALITY_COLOR(grade):
        grade = int(grade)
        if grade == 1:
            return "#1E90FF"
        elif grade == 2:
            return "#90EE90"
        elif grade == 3:
            return "#FF6347"
        else:
            return "#DC143C"

    def AIR_QUALITY_TEXT(grade):
        grade = int(grade)
        if grade == 1:
            return "좋음"
        elif grade == 2:
            return "보통"
        elif grade == 3:
            return "나쁨"
        else:
            return "매우 나쁨"

    IN_OUT_ERROR = "핸드폰이 꺼졌다가 켜진 것 같습니다ㅠㅠ"

    def TRANSLATED_TEXT(result):
        return f"번역된 결과는 다음과 같습니다. \n - {result}"

    FLOW_HAPPY = ":ear: 행복도 점수 대답을 기다리고 있습니다!"
    FLOW_ATTENTION = ":ear: 집중도 점수 대답을 기다리고 있습니다!"

    def PREDICT_RESULT(description):
        return f"지금은 왠지 *{description}* 기능을 사용하실 것 같군요!"
