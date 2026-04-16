import sqlite3
from datetime import datetime
from config.settings import DB_PATH

class EventLogger:
    def __init__(self):
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            scenario TEXT,
            event_type TEXT,
            person_id TEXT,
            color TEXT
        )
        """)
        self.conn.commit()

    def log(self, scenario, event_type, person_id="", color=""):
        self.conn.execute("""
        INSERT INTO events (timestamp, scenario, event_type, person_id, color)
        VALUES (?, ?, ?, ?, ?)
        """, (datetime.now().isoformat(), scenario, event_type, person_id, color))
        self.conn.commit()