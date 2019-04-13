from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
import re

app= Flask(__name__)
app.secret_key='keep it secret, keep it safe'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	if not EMAIL_REGEX.match(request.form['email']):
		flash("invalid email address")
		return redirect('/')
	else:
		mysql = connectToMySQL('email')
		query = 'INSERT INTO email (email, created_at, updated_at) VALUES (%(em)s, Now(), Now());'
		data = {
		'em': request.form['email']
		}

		id = mysql.query_db(query, data)

		return redirect('/success')

@app.route('/success', methods=['GET', 'POST'])
def success():
	mysql = connectToMySQL('email')
	emails = mysql.query_db('SELECT * FROM email;')

	return render_template('success.html', email=emails)


if __name__=="__main__":
	app.run(debug=True)