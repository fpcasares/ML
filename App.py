from flask import Flask
from flask import render_template
from ML import *

app = Flask(__name__)


@app.route('/api/v1')
def hello_world():
    return 'Welcome to OpinAPP initial version'


@app.route('/api/v1/get_products_by_name/<product_name>')
def products_list(product_name):
    product_list=get_products_by_name(product_name)
    return render_template('products.j2', product_list=product_list)
    
@app.route('/api/v1/get_reviews_by_product_id/<product_id>')
def review_list(product_id):
    review_list=get_reviews_by_product_id(product_id)
    if review_list != []:
        return render_template('reviews.j2', review_list=review_list)
    else:
        return 'Este producto no tiene opiniones'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5500')
