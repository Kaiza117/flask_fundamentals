from flask import Flask, session, render_template, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'shhh'

def random_number():
    session['num'] = random.randrange(0,101)


@app.route('/')
def index():
    session['num'] = random.randrange(0,101)
    print (session)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guessed_num = int(request.form['guess'])
    print (guessed_num)
    if guessed_num < session['num']:
        session['guessed_num'] = "low"
        print ("too low")
    elif guessed_num > session['num']:
        session['guessed_num'] = "high"
        print ("too high")
    else:
        session['guessed_num'] = "win"
        print ("You Guessed Right")
    return render_template('index.html')

@app.route('/reset')
def reset():
    session['guessed_num'] = ""
    random_number()
    return redirect('/')

app.run(debug=True)