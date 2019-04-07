from flask import Flask, render_template, request, redirect, session
import base64

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'




@app.route('/')
def home():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else: 
        session['visits'] = 1
    count = session.get('visits')
    return render_template('index.html', count=count)

@app.route('/destroy_session', methods=['POST', 'GET'])
def destroy():
    session.pop('visits', None)
    return redirect('/')

@app.route('/two')
def addTwo():
	session['visits'] = session.get('visits') + 1
	return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)