from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from utils import constants as const

class TrayIcon(QSystemTrayIcon):
    show_window = pyqtSignal()
    pause_timer = pyqtSignal()
    reset_timer = pyqtSignal()
    quit_app = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(const.TRAY_ICON_PATH))

        tray_menu = QMenu()

        show_action = QAction("Показать", tray_menu)
        show_action.triggered.connect(self.show_window.emit)
        tray_menu.addAction(show_action)

        pause_action = QAction("Пауза", tray_menu)
        pause_action.triggered.connect(self.pause_timer.emit)
        tray_menu.addAction(pause_action)

        reset_action = QAction("Сброс", tray_menu)
        reset_action.triggered.connect(self.reset_timer.emit)
        tray_menu.addAction(reset_action)

        quit_action = QAction("Выход", tray_menu)
        quit_action.triggered.connect(self.quit_app.emit)
        tray_menu.addAction(quit_action)

        self.setContextMenu(tray_menu)
        self.show()

    def show_notification(self, title, message, icon=QSystemTrayIcon.Information, duration=3000):
        self.showMessage(title, message, icon, duration)
