from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/')
def hello(name=None):
    return render_template('app.j2', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5500')
