import sqlite3
from config import DB_NAME

def add_expense(title, amount, category, date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
              (title, amount, category, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    data = c.fetchall()
    conn.close()
    return data
