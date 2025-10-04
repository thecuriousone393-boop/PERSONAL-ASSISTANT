import random
from flask import Blueprint, render_template, request

# Create a Blueprint for this game
guess_bp = Blueprint('guess', __name__, template_folder='templates')

@guess_bp.route('/guess', methods=['GET', 'POST'])
def guess_number():
    message = ""
    if request.method == 'POST':
        try:
            user_guess = int(request.form['guess'])
            number = random.randint(1, 10)

            if user_guess == number:
                message = f"🎉 Correct! The number was {number}."
            elif user_guess < number:
                message = f"Too low! The number was {number}. Try again."
            else:
                message = f"Too high! The number was {number}. Try again."
        except ValueError:
            message = "Please enter a valid number between 1 and 10."

    return render_template('guess.html', message=message)
