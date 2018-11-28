# wsgi.py
from flask import Flask
app = Flask(__name__)
from flask import jsonify

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' }
]

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS)
