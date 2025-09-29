import sqlite3
from config import DB_NAME

def get_response(user_message):
    user_message = user_message.lower()
    
    # Simple keyword-based responses
    if "hello" in user_message or "hi" in user_message:
        response = "Hello! How can I help you?"
    elif "time" in user_message:
        import datetime
        response = f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "joke" in user_message:
        response = "Why did the programmer go broke? Because he used up all his cache!"
    else:
        response = "Sorry, I don't understand."

    # Save chat to database
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO chatbot_logs (user_message, bot_response) VALUES (?, ?)",
              (user_message, response))
    conn.commit()
    conn.close()

    return response
