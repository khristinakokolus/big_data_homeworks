from flask import Flask, request
import json
import default_values
from data_selection import reviews_by_product, create_connection,\
    reviews_by_product_rating, reviews_by_customer

app = Flask(__name__)


@app.route('/')
def check_rest_api():
    return 'Hello from REST API'


@app.route('/reviews_by_product')
def get_reviews_by_product():
    client = create_connection()
    product_id = request.args.get('product_id')
    reviews = json.dumps(reviews_by_product(client, default_values.product_table, product_id))
    client.close()
    return reviews


@app.route('/reviews_by_product')
def get_reviews_by_product_rating():
    client = create_connection()
    product_id = request.args.get('product_id')
    star_rating = request.args.get('star_rating')
    reviews = json.dumps(reviews_by_product_rating(client, default_values.product_table, product_id, star_rating))
    client.close()
    return reviews


@app.route('/reviews_by_product')
def get_reviews_by_customer():
    client = create_connection()
    customer_id = request.args.get('customer_id')
    reviews = json.dumps(reviews_by_customer(client, default_values.product_table, customer_id))
    client.close()
    return reviews


@app.route('/reviews_by_product')
def get_most_reviewed_products():
    return "Most reviewed products"


@app.route('/reviews_by_product')
def get_most_active_customers():
    return "Most active customers"


@app.route('/reviews_by_product')
def get_haters():
    return "Haters"


@app.route('/reviews_by_product')
def get_backers():
    return "Bakers"


if __name__ == '__main__':
    app.run(debug=True)
