from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from utils import constants as const
from utils.logger import setup_logger

logger = setup_logger()

class TimerLogic(QObject):
    timer_updated = pyqtSignal(str)  # Emits formatted time string
    status_changed = pyqtSignal(str, str)  # Emits status text and style
    session_completed = pyqtSignal(int)  # Emits completed sessions count
    timer_finished = pyqtSignal(bool)  # Emits True if work session finished, False if break

    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.is_working = True
        self.is_running = False
        self.time_left = const.WORK_TIME_SECONDS
        self.session_count = 0
        self.completed_sessions = 0

        self.work_time = const.DEFAULT_WORK_TIME
        self.short_break = const.DEFAULT_SHORT_BREAK
        self.long_break = const.DEFAULT_LONG_BREAK
        self.sessions_before_long = const.DEFAULT_SESSIONS_BEFORE_LONG_BREAK

        logger.info("TimerLogic initialized")

    def set_times(self, work, short_break, long_break, sessions):
        self.work_time = work
        self.short_break = short_break
        self.long_break = long_break
        self.sessions_before_long = sessions
        if not self.is_running:
            self.reset()
        logger.info(f"Times updated: work={work}, short={short_break}, long={long_break}, sessions={sessions}")

    def start(self):
        if not self.is_running:
            self.timer.start(1000)
            self.is_running = True
            logger.info("Timer started")

    def pause(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            logger.info("Timer paused")

    def reset(self):
        self.timer.stop()
        self.is_running = False
        self.is_working = True
        self.time_left = self.work_time * 60
        self.session_count = 0
        self.status_changed.emit("Работа", const.STATUS_LABEL_WORK_STYLE)
        self.timer_updated.emit(self.format_time())
        logger.info("Timer reset")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_updated.emit(self.format_time())
        else:
            self.timer_finished_handler()

    def timer_finished_handler(self):
        self.timer.stop()
        self.is_running = False

        if self.is_working:
            self.completed_sessions += 1
            self.session_count += 1
            self.session_completed.emit(self.completed_sessions)

            if self.session_count >= self.sessions_before_long:
                self.is_working = False
                self.time_left = self.long_break * 60
                self.status_changed.emit("Длинный перерыв", const.STATUS_LABEL_BREAK_STYLE)
                self.session_count = 0
            else:
                self.is_working = False
                self.time_left = self.short_break * 60
                self.status_changed.emit("Короткий перерыв", const.STATUS_LABEL_BREAK_STYLE)

            self.timer_finished.emit(True)
            logger.info("Work session finished")
        else:
            self.is_working = True
            self.time_left = self.work_time * 60
            self.status_changed.emit("Работа", const.STATUS_LABEL_WORK_STYLE)
            self.timer_finished.emit(False)
            logger.info("Break session finished")

        self.timer_updated.emit(self.format_time())

    def format_time(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        return f"{minutes:02d}:{seconds:02d}"

    def is_timer_running(self):
        return self.is_running
