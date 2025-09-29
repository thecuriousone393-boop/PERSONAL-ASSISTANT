from flask import Flask, render_template

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

@app.route('/chatbot/message', methods=['POST'])
def chatbot_message():
    data = request.json
    msg = data.get('message', '')
    chatbot.save_chat('user', msg)
    resp = chatbot.simple_response(msg)
    chatbot.save_chat('bot', resp)
    return jsonify({"reply": resp})
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
    

