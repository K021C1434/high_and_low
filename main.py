from flask import Flask, render_template
import random

app = Flask(__name__)

card = 0

@app.route('/')
def index():
    # データを指定 --- (*1)
    global card
    card = random.randint(1,13)

    # テンプレートエンジンにデータを指定 --- (*2)
    return render_template('index.html',
            card=card)

@app.route('/high')
def high():
    # データを指定 --- (*1)
    random_number = random.randint(1, 13)
    global card
    if card < random_number:
      result = "You Lose"
    else:
      result = "You Win!"
    # テンプレートエンジンにデータを指定 --- (*2)
    return render_template('high.html', result= result, random_number=random_number)


@app.route('/low')
def low():
    # データを指定 --- (*1)
    random_number = random.randint(1, 13)
    global card
    if card < random_number:
      result="You Win!"
    else:
      result = "You Lose"


    # テンプレートエンジンにデータを指定 --- (*2)
    return render_template('low.html',
            result=result, random_number=random_number)
app.run(host='0.0.0.0')

