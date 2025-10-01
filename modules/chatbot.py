from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Chatbot page
@app.route('/chatbot')
def chatbot_page():
    return render_template('chatbot.html')

# API for chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message")  # get message from frontend

    # Simple logic for chatbot replies (you can expand later)
    if "hello" in msg or "hi" in msg:
        bot_reply = "Hello 👋! How can I assist you today?"
    elif "bye" in msg:
        bot_reply = "Goodbye! Have a great day 😊"
    elif "how are you" in msg:
        bot_reply = "I’m doing great, thanks for asking! How about you?"
    elif "your name" in msg:
        bot_reply = "I’m your smart assistant 🤖."
    elif "weather" in msg:
        bot_reply = "You can check the Weather page in the app 🌦️."
    elif "expense" in msg:
        bot_reply = "Head over to the Expense Tracker page 💰."
    elif "todo" in msg or "task" in msg:
        bot_reply = "Your To-Do List is waiting! ✅"
    else:
        bot_reply = "Hmm 🤔 I don’t know that yet, but I’ll learn soon!"
    return jsonify({"reply": bot_reply})


