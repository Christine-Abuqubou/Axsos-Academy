 
from flask import Flask

app = Flask(__name__)

#  1"Hello World!"
@app.route('/')
def home():
    return "Hello World!"

# 2"Champion!"
@app.route('/Champion')
def Champion():
    return "Champion!"


@app.route('/say/Flask')
def say_flask():
    return "Hi Flask!"
@app.route('/say/Micheal')
def say_Micheal():
    return "Hi Micheal!"
@app.route('/say/John')
def say_John():
    return "Hi John!"

@app.route('/repeat/35/hello')
def hello():
    return ("hello <br>"*35)

@app.route('/repeat/80/bye')
def bye():
    return ("bye <br>"*80)

@app.route('/repeat/99/dogs')
def dogs():
    return ("dogs <br>"*99)


if __name__ == '__main__':
    app.run(debug=True)