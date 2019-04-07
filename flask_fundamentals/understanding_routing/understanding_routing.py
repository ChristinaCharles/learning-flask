from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello_three(name):
    # if type(name) == 
    if name.isalpha():
        return 'Hello ' + name + '!'
    else:
        return 'Sorry! No response. Try again.'

@app.route('/repeat/<num>/<word>')
def repeated_word(num, word):
    if word.isalpha() and num.isdigit():
        return word * int(num)
    else:
        return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
