import json
import os
from utils import constants as const
from utils.logger import setup_logger

logger = setup_logger()

class DataManager:
    def __init__(self):
        self.data_dir = 'data'
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            logger.info("Created data directory")

        self.sessions_file = os.path.join(self.data_dir, 'sessions.json')
        self.settings_file = os.path.join(self.data_dir, 'settings.json')

        self.sessions = self.load_sessions()
        self.settings = self.load_settings()

    def load_sessions(self):
        try:
            if os.path.exists(self.sessions_file):
                with open(self.sessions_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    logger.info("Loaded sessions data")
                    return data
            else:
                logger.info("Sessions file not found, starting with empty sessions")
                return []
        except Exception as e:
            logger.error(f"Error loading sessions: {e}")
            return []

    def save_sessions(self):
        try:
            with open(self.sessions_file, 'w', encoding='utf-8') as f:
                json.dump(self.sessions, f, indent=2, ensure_ascii=False)
            logger.info("Saved sessions data")
        except Exception as e:
            logger.error(f"Error saving sessions: {e}")

    def load_settings(self):
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    logger.info("Loaded settings data")
                    return data
            else:
                logger.info("Settings file not found, using defaults")
                return {
                    'work_time': const.DEFAULT_WORK_TIME,
                    'short_break': const.DEFAULT_SHORT_BREAK,
                    'long_break': const.DEFAULT_LONG_BREAK,
                    'sessions_before_long': const.DEFAULT_SESSIONS_BEFORE_LONG_BREAK
                }
        except Exception as e:
            logger.error(f"Error loading settings: {e}")
            return {
                'work_time': const.DEFAULT_WORK_TIME,
                'short_break': const.DEFAULT_SHORT_BREAK,
                'long_break': const.DEFAULT_LONG_BREAK,
                'sessions_before_long': const.DEFAULT_SESSIONS_BEFORE_LONG_BREAK
            }

    def save_settings(self):
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
            logger.info("Saved settings data")
        except Exception as e:
            logger.error(f"Error saving settings: {e}")

    def add_session(self, session_type, duration):
        session = {
            'type': session_type,
            'duration': duration,
            'timestamp': self.get_current_timestamp()
        }
        self.sessions.append(session)
        self.save_sessions()
        logger.info(f"Added session: {session}")

    def get_sessions_count(self):
        return len([s for s in self.sessions if s['type'] == 'work'])

    def get_settings(self):
        return self.settings.copy()

    def update_settings(self, work, short, long, sessions):
        self.settings = {
            'work_time': work,
            'short_break': short,
            'long_break': long,
            'sessions_before_long': sessions
        }
        self.save_settings()
        logger.info(f"Updated settings: {self.settings}")

    def get_current_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()
