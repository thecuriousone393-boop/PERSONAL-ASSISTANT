# 🧑‍💻 Smart Personal Assistant (Flask Project)

An **All-in-One Smart Personal Assistant App** built with **Flask, SQLite, HTML, CSS, and JavaScript**.  
It includes 5 modules: **Expense Tracker, To-Do List, Quiz Game, Chatbot, and Weather Info**.

---

## 🚀 Features
- **Expense Tracker** → Add, view, and delete expenses, with total calculation.  
- **To-Do List** → Add tasks, mark them as done, or delete them.  
- **Fun corner** → Place to relax and have Fun.  
- **Chatbot** → Simple rule-based chatbot with logging.  
- **Weather Info** → Fetch live weather by city (uses OpenWeather API).  

---

## 📂 Project Structure

-Main folder name: SmartAssistant

-->Inside it, create these files:

-app.py (main file to run the app)

-config.py (settings like API keys and database path)

-requirements.txt (list of required Python packages)

-README.md (project documentation)

-->Create a folder named modules → put these files inside:

db_init.py

expense_tracker.py

todo.py

quiz.py

chatbot.py

weather.py

-->Create a folder named templates → put these HTML files inside:

base.html

index.html

expenses.html

todo.html

quiz.html

chatbot.html

weather.html

error.html

-->Create a folder named static → put design files inside:

style.css (for CSS styles)

script.js (for JavaScript)

optionally a subfolder called assets for images/icons


## 🧠 Basic Logic Behind Each Module
1️⃣ Expense Tracker

Data stored in SQLite table expenses.

Each expense = title + amount + category + date.

Add expense → Insert into DB.

List expenses → SELECT * FROM expenses ORDER BY id DESC.

Delete expense → DELETE FROM expenses WHERE id = ?.

Total expenses → SUM(amount) query.

2️⃣ To-Do List

Stored in SQLite table todos.

Each task has id + task + done (0/1).

Add task → Insert with done = 0.

Mark done → Update row with done = 1.

Delete task → Remove row by id.

3️⃣ Quiz Game

Multiple fun games are added>

joke box -> displays random jokes when 'get joke' button in pressed.

guess the number -> starts a game where user has to guess the number between '1 to 10'.

4️⃣ Chatbot

Very simple rule-based chatbot.

User message stored in DB chats (role=user, message).

Bot checks for keywords:

"hello" → Greeting

"time" → Current time

"joke" → Small joke

"help" → Available features

Else → "Sorry, I don’t understand."

Bot’s reply also stored in DB (role=bot, message).

5️⃣ Weather Module

Uses OpenWeather API.

User enters city → JS sends request to Flask → Flask calls API with requests.

Response parsed → city, temp, description, humidity, wind.

If API key missing or city invalid → return error message.







## 🖥️ Usage

Home Page → Navigate to different modules.

Expenses → Enter title, amount, category, and date → Add expense.

To-Do → Add tasks → Mark done or delete.

Fun -> Relax and play fun games.

Chatbot → Send a message → Get bot response.

Weather → Enter city name → Fetch weather details.



## 🧩 Future Improvements

User authentication (login/signup)

CSV export of expenses

Better chatbot with AI responses

UI improvements with Bootstrap
