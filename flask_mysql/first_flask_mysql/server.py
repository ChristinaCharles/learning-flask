from flask import Flask, render_template
from mysqlconnection import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')           # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
            
if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/')
# def index():
#     mysql = connectToMySQL("first_flask")
#     friends = mysql.query_db("SELECT * FROM friends;")
#     print(friends)
#     return render_template("index.html", all_friends = friends)