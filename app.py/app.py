from flask import Flask, render_template,request,jsonify

app=Flask(__name__)

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
@app.route('/weather')
def weather():
    return render_template('weather.html')
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

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
    

