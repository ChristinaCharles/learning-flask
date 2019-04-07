from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def blue_boxes():
    return render_template('index.html', times=3)

@app.route('/play/<num>')
def num_boxes(num):
    number = int(num)
    return render_template('index.html', times=number)

@app.route('/play/<num>/<color>')
def color_boxes(num, color):
    number = int(num)
    return render_template('index.html', times=number, color=color)

if __name__ == "__main__":
    app.run(debug=True)