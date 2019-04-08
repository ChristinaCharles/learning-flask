from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.seccret_key = 'keey it secret, keep it safe'

@app.route('/', methods=['POST', 'GET'])
def home(guess=None):
	num = random.randint(1,100)
	if guess != None: 
		if num > int(guess):
			color = 'red'

	return render_template('index.html', num=num, guess=guess)

@app.route('/guess', methods=['POST', 'GET'])
def guess():
	guess = int(request.form['guess'])
	num = int(request.form['num'])
	if guess > num:
		key = 'high'
		message = "too high"
		color = 'red'
	elif guess < num:
		key = 'low'
		message = "too low"
		color = 'red'
	else:
		key='right'
		message = str(num) + " was the number!"
		color = 'green'

	return render_template('index.html', guess=guess, num=num, message=message, color=color, key=key)


if __name__=="__main__":
	app.run(debug=True)