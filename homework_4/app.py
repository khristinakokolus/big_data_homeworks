from flask import Flask, request
import json
import default_values
from data_selection import reviews_by_product, create_connection

app = Flask(__name__)


@app.route('/')
def check_rest_api():
    return 'Hello from REST API'


@app.route('/reviews_by_product')
def get_reviews_by_product():
    print("here")
    client = create_connection()
    product_id = request.args.get('product_id')
    reviews = json.dumps(reviews_by_product(client, default_values.product_table, product_id))
    client.close()
    return reviews


@app.route('/reviews_by_product')
def get_reviews_by_product_rating():
    return None


@app.route('/reviews_by_product')
def get_reviews_by_customer():
    return None


@app.route('/reviews_by_product')
def get_most_reviewed_products():
    return None


@app.route('/reviews_by_product')
def get_most_active_customers():
    return None


@app.route('/reviews_by_product')
def get_haters():
    return None


@app.route('/reviews_by_product')
def get_backers():
    return None


if __name__ == '__main__':
    app.run(debug=True)
