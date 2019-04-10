from flask import Flask, render_template, request, redirect, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    is_valid = True

    if not name_regex.match(request.form['fname']) or len(request.form['fname']) < 1:
        flash('Please enter a valid first name')
        is_valid = False

    if not name_regex.match(request.form['lname']) or len(request.form['lname']) < 1:
        flash('Please enter a valid last name')
        is_valid = False

    if not EMAIL_REGEX.match(request.form['email']):
        flash("invalid email address")
        is_valid = False
    if len(request.form['password']) < 1:
        flash('Please enter a password')
        is_valid = False

    if request.form['password'] != request.form['pconfirm']:
        flash('Passwords must match')
        is_valid = False

    if is_valid == False:
        return redirect('/')

    else:
        pword = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL('login_registration')
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, Now(), Now());'
        data = {
            'fn': request.form['fname'],
            'ln': request.form['lname'],
            'em': request.form['email'],
            'pw': pword
        }
        mysql.query_db(query, data)

        flash('You\'ve been successfully registered!')
        session['name'] = request.form['fname']


    return redirect('/success')

@app.route('/success', methods=["GET", 'POST'])
def success():
    name = session.get('name')

    if name == None:
        flash('please login')
        return redirect('/')

    return render_template('success.html', name=name)

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('name', None)
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    mysql = connectToMySQL('login_registration')
    query = 'SELECT * FROM users;'
    user = mysql.query_db(query)

    # name = session.get('name')

    for u in user:
        if request.form['loginEmail'] in u['email']:
            if bcrypt.check_password_hash(u['password'], request.form['loginPassword']):
                name = u['first_name']
                session['name'] = u['first_name']


                return render_template('success.html', name=name)

    flash('Please register')

    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)





