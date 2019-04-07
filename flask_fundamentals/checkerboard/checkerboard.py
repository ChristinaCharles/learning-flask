from flask import Flask, render_template
app = Flask(__name__)

# def checkerboard():
# 	return render_template('index.html')

@app.route('/')
@app.route('/<x>/<y>')
@app.route('/<x>/<y>')
@app.route('/<x>/<y>/<color1>/<color2>')
def checker_row(x=4,y=4, color1='red', color2='black'):
	x = int(x)
	y = int(y)
	colors = [color1, color2]
	return render_template('index.html', rows = x, cols = y, color=colors)

if __name__=="__main__":
	app.run(debug=True)