from flask import Flask, request
import requests
from data_selection import reviews_by_product, create_connection

PRODUCT_TABLE = "product_statistics"
CUSTOMER_TABLE = "customer_statistics"
HATERS_HACKERS_TABLE = "haters_backers"

app = Flask(__name__)


@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


@app.route('/reviews_by_product')
def get_answer():
    print("here")
    client = create_connection(PRODUCT_TABLE)
    product_id = request.args.get('product_id')
    print("stated")
    return reviews_by_product(client, PRODUCT_TABLE, product_id)


@app.route('/reviews_data')
def post_constrains():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
