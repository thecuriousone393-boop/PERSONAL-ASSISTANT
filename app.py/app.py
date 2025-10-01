from flask import Flask, render_template,request,jsonify
import random

app=Flask(__name__)

tasks = []

jokes_list = [
    "Why don’t scientists trust atoms? Because they make up everything! 😆",
    "Teacher: Why are you late? Student: Because of the sign on the road. Teacher: What sign? Student: 'School Ahead, Go Slow!' 😂",
    "Why was the math book sad? Because it had too many problems 📘😢",
    "Pappu: 'Mom, can I have money for the school trip?' Mom: 'Sure beta, where are you going?' Pappu: 'To the canteen.' 🤭",
    "Why did the computer go to the doctor? Because it caught a virus 🖥️🤒"
    "Santa: 'Do you know why Indians don’t play hide and seek?' Banta: 'Why?' Santa: 'Because no one can hide when aunties are around asking ‘Beta, shaadi kab karoge?’ 🤣",
    "Teacher: 'Where is Taj Mahal?' Student: 'In WhatsApp DP of every second person!' 📱😂",
    "Pappu in exam: 'Can I have marks for neat handwriting?' Teacher: 'Beta, this is a math paper, not calligraphy!' ✍️🤣",
    "Santa ordered pizza. Waiter: 'Sir, should I cut it into 6 pieces or 8?' Santa: '6 is fine, I can’t eat 8 pieces.' 🍕😂",
    "Bollywood version of Physics: Every action has an equal and opposite overacting! 🎬🤣",
    "Indian Dad after seeing electricity bill: 'Beta, are you running a disco at home?' 💡😂",
    "Wife: 'Listen, the doorbell is ringing.' Husband: 'So? We didn’t invite anyone.' Wife: 'Amazon delivery!' Husband: 'I’M COMINGGG!' 📦😂",
]

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/expenses')
def expenses():
    return render_template('expenses.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message")  

    if not user_input:
        return jsonify({"reply": "Sorry, I didn’t catch that."})

    # Convert input to lowercase for easier matching
    msg = user_input.lower()

    # Rule-based replies
    if "hello" in msg or "hi" in msg:
        bot_reply = "Hello 👋! How can I assist you today?"
    elif "bye" in msg:
        bot_reply = "Goodbye! Have a great day 😊"
    elif "how are you" in msg:
        bot_reply = "I’m doing great, thanks for asking! How about you?"
    elif "your name" in msg or "who are you" in msg:
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


@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# API to add a task
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.json.get("task")
    if task:
        tasks.append(task)
        return jsonify({"message": "Task added!", "tasks": tasks})
    return jsonify({"message": "Task cannot be empty!"}), 400

# API to delete a task
@app.route('/delete_task', methods=['POST'])
def delete_task():
    task = request.json.get("task")
    if task in tasks:
        tasks.remove(task)
        return jsonify({"message": "Task deleted!", "tasks": tasks})
    return jsonify({"message": "Task not found!"}), 404




@app.route('/weather')
def weather():
    return render_template('weather.html')
@app.route('/fun')
def fun():
    return render_template('fun.html')


# Sample jokes (you can add more later)


@app.route('/fun/get_joke')
def get_random_joke():
    joke = random.choice(jokes_list)
    return jsonify({"joke": joke})

if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
from flask import request, redirect
from modules import expense_tracker

@app.route("/expenses", methods=["GET", "POST"])
def expenses():
    if request.method == "POST":
        title = request.form["title"]
        amount = request.form["amount"]
        category = request.form["category"]
        date = request.form["date"]
        expense_tracker.add_expense(title, amount, category, date)
        return redirect("/expenses")
    data = expense_tracker.get_expenses()
    return render_template("expenses.html", expenses=data)
    

