import sqlite3
from config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Expenses table
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    amount REAL,
                    category TEXT,
                    date TEXT)''')

    # To-Do table
    c.execute('''CREATE TABLE IF NOT EXISTS todo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT,
                    status TEXT)''')

    # Chatbot logs
    c.execute('''CREATE TABLE IF NOT EXISTS chatbot_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_message TEXT,
                    bot_response TEXT)''')

    conn.commit()
    conn.close()

init_db()
