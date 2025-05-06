from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    options = ['가위','바위','보']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = '비겼습니다'
    elif (user_choice == '가위' and computer_choice == '보') or \
    (user_choice == '바위' and computer_choice == '가위') or \
    (user_choice == '보' and computer_choice == '바위') :
        result = '당신이 이겼습니다'
    else :
        result = '당신이 졌습니다'

    return render_template('result.html', user=user_choice, computer=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)