from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/users", methods=["GET"])
def index():
    mysql = connectToMySQL('users')
    users = mysql.query_db('SELECT * FROM users;')
    return render_template('index.html', users=users)

@app.route("/users/new", methods=["GET"])
def new():
    return render_template('new.html')

@app.route("/users/create", methods=["POST"])
def create():
    mysql = connectToMySQL('users')
    query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());' 
    data = {
    'fn': request.form['fname'],
    'ln': request.form['lname'],
    'em': request.form['email']
    } 

    id = mysql.query_db(query, data)
    num = str(id)

    return redirect('/users/'+num)

@app.route('/users/<id>', methods=["GET"])
def user_id(id):
    num = int(id)
    mysql = connectToMySQL('users')
    user = mysql.query_db('SELECT * FROM users WHERE id = %(id)s;', {'id': num})

    return render_template('user_id.html', user=user)

@app.route('/users/<id>/edit', methods=["GET"])
def edit(id):
    num=int(id)
    mysql = connectToMySQL('users')
    user = mysql.query_db('SELECT * FROM users WHERE id = %(id)s;', {'id': num})
    return render_template('edit.html', user=user)

@app.route('/users/<id>/update', methods=["POST"])
def update(id):
    num = int(id)
    mysql = connectToMySQL('users')
    query = 'UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email = %(em)s, created_at = Now(), updated_at = Now() WHERE id = %(id)s;'
    data = {
    'fn': request.form['fname'],
    'ln': request.form['lname'],
    'em': request.form['email'],
    'id': num
    }
    mysql.query_db(query, data)
    return redirect('/users/'+id)

@app.route('/users/<id>/destroy', methods=["GET"])
def destroy(id):
    num = int(id)
    mysql = connectToMySQL('users')
    mysql.query_db('DELETE FROM users WHERE id = %(id)s;', {'id': num})
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True)



