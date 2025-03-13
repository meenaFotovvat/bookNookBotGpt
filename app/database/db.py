import sqlite3

DB_NAME = "booknook.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            channel TEXT,
            message_id INTEGER,
            text TEXT,
            date TEXT,
            sender_id INTEGER
        )
    ''')
    conn.commit()
    conn.close()
