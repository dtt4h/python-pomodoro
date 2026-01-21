import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PyQt5.QtGui import QIcon
from controllers.controller import PomodoroController
from utils import constants as const
from utils.logger import setup_logger

logger = setup_logger()

class PomodoroApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setApplicationName(const.WINDOW_TITLE)

        if QSystemTrayIcon.isSystemTrayAvailable():
            self.app.setWindowIcon(QIcon(const.TRAY_ICON_PATH))

        self.controller = PomodoroController()
        logger.info("Pomodoro App initialized")

    def run(self):
        self.controller.ui.show()
        sys.exit(self.app.exec_())

def main():
    pomodoro_app = PomodoroApp()
    pomodoro_app.run()

if __name__ == '__main__':
    main()
