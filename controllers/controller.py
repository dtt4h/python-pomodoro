from models.timer_logic import TimerLogic
from models.data_manager import DataManager
from views.ui import PomodoroUI
from views.tray_icon import TrayIcon
from utils.logger import setup_logger

logger = setup_logger()

class PomodoroController:
    def __init__(self):
        self.data_manager = DataManager()
        self.timer_logic = TimerLogic(self.data_manager)
        self.ui = PomodoroUI()
        self.tray = TrayIcon()

        self.connect_signals()
        self.load_initial_data()
        logger.info("Controller initialized")

    def connect_signals(self):
        # UI to controller
        self.ui.start_clicked.connect(self.start_timer)
        self.ui.pause_clicked.connect(self.pause_timer)
        self.ui.reset_clicked.connect(self.reset_timer)
        self.ui.times_changed.connect(self.update_settings)

        # Logic to UI
        self.timer_logic.timer_updated.connect(self.ui.update_timer_display)
        self.timer_logic.status_changed.connect(self.ui.update_status)
        self.timer_logic.session_completed.connect(self.ui.update_stats)
        self.timer_logic.timer_finished.connect(self.handle_timer_finished)

        # Tray to controller
        self.tray.show_window.connect(self.show_window)
        self.tray.pause_timer.connect(self.pause_timer)
        self.tray.reset_timer.connect(self.reset_timer)
        self.tray.quit_app.connect(self.quit_app)

        # UI close to tray
        self.ui.closeEvent = self.handle_close_event

    def load_initial_data(self):
        settings = self.data_manager.get_settings()
        self.timer_logic.set_times(
            settings['work_time'],
            settings['short_break'],
            settings['long_break'],
            settings['sessions_before_long']
        )
        self.ui.set_initial_times(settings)
        self.ui.update_stats(self.data_manager.get_sessions_count())

    def start_timer(self):
        self.timer_logic.start()
        self.ui.set_buttons_state(True)
        logger.info("Timer started")

    def pause_timer(self):
        self.timer_logic.pause()
        self.ui.set_buttons_state(False)
        logger.info("Timer paused")

    def reset_timer(self):
        self.timer_logic.reset()
        self.ui.set_buttons_state(False)
        logger.info("Timer reset")

    def update_settings(self, work, short, long, sessions):
        self.timer_logic.set_times(work, short, long, sessions)
        self.data_manager.update_settings(work, short, long, sessions)

    def handle_timer_finished(self, is_work_finished):
        if is_work_finished:
            duration = self.timer_logic.work_time
            self.data_manager.add_session('work', duration)
        else:
            duration = self.timer_logic.long_break if self.timer_logic.session_count == 0 else self.timer_logic.short_break
            self.data_manager.add_session('break', duration)

        self.ui.update_stats(self.data_manager.get_sessions_count())
        self.tray.show_notification("Pomodoro Timer", "Session completed!")
        self.ui.set_buttons_state(False)

    def show_window(self):
        self.ui.show()

    def handle_close_event(self, event):
        event.ignore()
        self.ui.hide()
        self.tray.show_notification("Pomodoro Timer", "App minimized to tray")

    def quit_app(self):
        logger.info("App quitting")
        # Save any pending data
        self.data_manager.save_sessions()
        self.data_manager.save_settings()
        # Quit the app
        from PyQt5.QtWidgets import QApplication
        QApplication.quit()
