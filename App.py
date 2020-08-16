from flask import Flask
from flask import render_template
from ML import *

app = Flask(__name__)


@app.route('/api/v1')
def hello_world():
    return 'Welcome to OpinAPP initial version'


@app.route('/api/v1/get_product_by_name/<product_name>')
def hello(product_name):
    product_list=get_products_by_name(product_name)
    return render_template('APP.j2', product_list=product_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5500')
