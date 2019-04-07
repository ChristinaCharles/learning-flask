from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def home():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	name_form = request.form['name']
	loc = request.form['loc']
	lang = request.form['language']
	text = request.form['text']
	return render_template('show.html', name_form=name_form, loc=loc, lang=lang, text=text)


if __name__=="__main__":
	app.run(debug=True)