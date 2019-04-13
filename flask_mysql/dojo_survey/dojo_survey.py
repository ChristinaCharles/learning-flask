from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'



@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("Please enter a name")

    if len(request.form['loc']) < 1:
        is_valid = False
        flash("Please enter a location")

    if len(request.form['language']) < 1:
        is_valid = False
        flash("Please enter a language")

    if is_valid == False:
        return redirect('/')
    
    else:
        mysql = connectToMySQL('dojos')
        query = 'INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(nam)s, %(loc)s, %(lang)s, %(txt)s, Now(), Now());'
        data = {
        'nam':request.form['name'],
        'loc': request.form['loc'],
        'lang': request.form['language'],
        'txt': request.form['text']
        }
        id = mysql.query_db(query, data)

        nam = request.form['name']
        loc = request.form['loc']
        lang = request.form['language']
        txt = request.form['text']
        # flash("success")

        return render_template('show.html', nam=nam, loc=loc, lang=lang, txt=txt)



if __name__=="__main__":
    app.run(debug=True)