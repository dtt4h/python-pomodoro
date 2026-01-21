from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from utils import constants as const

class PomodoroUI(QMainWindow):
    start_clicked = pyqtSignal()
    pause_clicked = pyqtSignal()
    reset_clicked = pyqtSignal()
    times_changed = pyqtSignal(int, int, int, int)  # work, short, long, sessions

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(const.WINDOW_TITLE)
        self.setGeometry(*const.WINDOW_GEOMETRY)
        self.setStyleSheet(const.MAIN_WINDOW_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(24)
        main_layout.setContentsMargins(32, 32, 32, 32)

        # Timer label
        self.timer_label = QLabel("25:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet(const.TIMER_LABEL_STYLE)
        main_layout.addWidget(self.timer_label)

        # Status label
        self.status_label = QLabel("Работа")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet(const.STATUS_LABEL_WORK_STYLE)
        main_layout.addWidget(self.status_label)

        # Buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(16)

        self.start_button = QPushButton("Старт")
        self.start_button.setObjectName("startButton")
        self.start_button.clicked.connect(self.start_clicked.emit)

        self.pause_button = QPushButton("Пауза")
        self.pause_button.setObjectName("pauseButton")
        self.pause_button.clicked.connect(self.pause_clicked.emit)
        self.pause_button.setEnabled(False)

        self.reset_button = QPushButton("Сброс")
        self.reset_button.setObjectName("resetButton")
        self.reset_button.clicked.connect(self.reset_clicked.emit)

        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.pause_button)
        buttons_layout.addWidget(self.reset_button)
        main_layout.addLayout(buttons_layout)

        # Settings group
        settings_group = QGroupBox("Настройка интервалов")
        settings_layout = QGridLayout()
        settings_layout.setSpacing(12)

        settings_layout.addWidget(QLabel("Работа (мин):"), 0, 0)
        self.work_time_input = QSpinBox()
        self.work_time_input.setRange(1, 60)
        self.work_time_input.setValue(const.DEFAULT_WORK_TIME)
        self.work_time_input.valueChanged.connect(self.emit_times_changed)
        settings_layout.addWidget(self.work_time_input, 0, 1)

        settings_layout.addWidget(QLabel("Короткий перерыв (мин):"), 1, 0)
        self.short_break_input = QSpinBox()
        self.short_break_input.setRange(1, 30)
        self.short_break_input.setValue(const.DEFAULT_SHORT_BREAK)
        self.short_break_input.valueChanged.connect(self.emit_times_changed)
        settings_layout.addWidget(self.short_break_input, 1, 1)

        settings_layout.addWidget(QLabel("Длинный перерыв (мин):"), 2, 0)
        self.long_break_input = QSpinBox()
        self.long_break_input.setRange(1, 60)
        self.long_break_input.setValue(const.DEFAULT_LONG_BREAK)
        self.long_break_input.valueChanged.connect(self.emit_times_changed)
        settings_layout.addWidget(self.long_break_input, 2, 1)

        settings_layout.addWidget(QLabel("Сессии до длинного перерыва:"), 3, 0)
        self.sessions_input = QSpinBox()
        self.sessions_input.setRange(1, 10)
        self.sessions_input.setValue(const.DEFAULT_SESSIONS_BEFORE_LONG_BREAK)
        self.sessions_input.valueChanged.connect(self.emit_times_changed)
        settings_layout.addWidget(self.sessions_input, 3, 1)

        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)

        # Stats
        stats_layout = QHBoxLayout()
        self.stats_label = QLabel("Сессий завершено: 0")
        self.stats_label.setStyleSheet(const.STATS_LABEL_STYLE)
        stats_layout.addWidget(self.stats_label)
        main_layout.addLayout(stats_layout)

    def emit_times_changed(self):
        self.times_changed.emit(
            self.work_time_input.value(),
            self.short_break_input.value(),
            self.long_break_input.value(),
            self.sessions_input.value()
        )

    def set_initial_times(self, settings):
        self.work_time_input.setValue(settings['work_time'])
        self.short_break_input.setValue(settings['short_break'])
        self.long_break_input.setValue(settings['long_break'])
        self.sessions_input.setValue(settings['sessions_before_long'])

    def update_timer_display(self, time_str):
        self.timer_label.setText(time_str)

    def update_status(self, text, style):
        self.status_label.setText(text)
        self.status_label.setStyleSheet(style)

    def update_stats(self, count):
        self.stats_label.setText(f"Сессий завершено: {count}")

    def set_buttons_state(self, is_running):
        self.start_button.setEnabled(not is_running)
        self.pause_button.setEnabled(is_running)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
