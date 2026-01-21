# Constants for the Pomodoro Timer application

# Default timer values (in minutes)
DEFAULT_WORK_TIME = 25
DEFAULT_SHORT_BREAK = 5
DEFAULT_LONG_BREAK = 15
DEFAULT_SESSIONS_BEFORE_LONG_BREAK = 4

# Timer intervals in seconds
WORK_TIME_SECONDS = DEFAULT_WORK_TIME * 60
SHORT_BREAK_SECONDS = DEFAULT_SHORT_BREAK * 60
LONG_BREAK_SECONDS = DEFAULT_LONG_BREAK * 60

# UI Styles - Dark Minimalist Design
MAIN_WINDOW_STYLE = """
    QMainWindow {
        background-color: #121212;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    QWidget {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    QLabel {
        color: #ffffff;
        font-size: 14px;
    }
    QLineEdit {
        background-color: #1e1e1e;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 8px 12px;
        color: #ffffff;
        font-size: 14px;
    }
    QLineEdit:focus {
        border-color: #007bff;
        box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
    }
    QPushButton {
        background-color: #1e1e1e;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 12px 24px;
        color: #ffffff;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    QPushButton:hover {
        background-color: #2a2a2a;
        border-color: #555;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    QPushButton:pressed {
        background-color: #333;
        transform: translateY(0);
    }
    QPushButton#startButton {
        background-color: #4caf50;
        color: #ffffff;
        border-color: #4caf50;
    }
    QPushButton#startButton:hover {
        background-color: #45a049;
        border-color: #45a049;
    }
    QPushButton#pauseButton {
        background-color: #ff9800;
        color: #ffffff;
        border-color: #ff9800;
    }
    QPushButton#pauseButton:hover {
        background-color: #e68900;
        border-color: #e68900;
    }
    QPushButton#resetButton {
        background-color: #f44336;
        color: #ffffff;
        border-color: #f44336;
    }
    QPushButton#resetButton:hover {
        background-color: #d32f2f;
        border-color: #d32f2f;
    }
    QSpinBox {
        background-color: #1e1e1e;
        border: 1px solid #333;
        border-radius: 8px;
        color: #ffffff;
        padding: 8px 12px;
        font-size: 14px;
    }
    QSpinBox:focus {
        border-color: #007bff;
        box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
    }
    QGroupBox {
        border: 1px solid #333;
        border-radius: 12px;
        margin-top: 16px;
        padding-top: 16px;
        color: #ffffff;
        font-size: 16px;
        font-weight: 600;
        background-color: #1e1e1e;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 12px;
        padding: 0 8px 0 8px;
        color: #cccccc;
    }
"""

TIMER_LABEL_STYLE = """
    font-size: 64px;
    font-weight: 300;
    color: #ffffff;
    padding: 24px;
    background-color: #1e1e1e;
    border-radius: 12px;
    border: 1px solid #333;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
"""

STATUS_LABEL_WORK_STYLE = """
    font-size: 16px;
    font-weight: 500;
    color: #64b5f6;
    padding: 8px 0;
    background-color: transparent;
"""

STATUS_LABEL_BREAK_STYLE = """
    font-size: 16px;
    font-weight: 500;
    color: #81c784;
    padding: 8px 0;
    background-color: transparent;
"""

STATS_LABEL_STYLE = "font-size: 12px; color: #aaaaaa; font-weight: 400;"

# Window settings
WINDOW_TITLE = 'Pomodoro Timer'
WINDOW_GEOMETRY = (300, 300, 420, 550)

# Tray icon path (placeholder)
TRAY_ICON_PATH = ":/icons/timer.png"

# Notification messages
NOTIFICATION_SESSION_FINISHED = "Session completed!"
NOTIFICATION_SESSION_STARTED = "Break time!"
NOTIFICATION_APP_MINIMIZED = "App minimized to tray"

# Data files
SESSIONS_FILE = 'data/sessions.json'
SETTINGS_FILE = 'data/settings.json'
