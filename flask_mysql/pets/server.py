from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    # print(pets)
    return render_template('index.html', pets=pets)

@app.route('/add_pet', methods=['POST', 'GET'])
def add_pet():
    mysql = connectToMySQL('pets')
    query = 'INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(na)s, %(ty)s, NOW(), NOW());' 
    data = {
    'na': request.form['pname'],
    'ty': request.form['type'],
    } 
    # print(request.form)
    # nam = request.form['type']

    pet_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)