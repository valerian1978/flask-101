# wsgi.py
from flask import Flask, jsonify, abort, request
from flask_api import status
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Breizh.tv' },
]

class Counter:
    def __init__(self):
        self.id = 0
        for p in PRODUCTS:
            if self.id < p['id']:
                self.id = p['id']

    def next(self):
        self.id += 1
        return self.id

ID = Counter()

@app.route('/')
def hello():
    return "Hello Mad World!"

@app.route('/api/v1/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return jsonify(PRODUCTS)

    product = request.get_json()
    pro = {
      'id': ID.next(),
      'name': product['name'],
    }
    PRODUCTS.append(pro)
    return jsonify(pro), status.HTTP_201_CREATED


@app.route('/api/v1/products/<int:product_id>', methods=['GET', 'DELETE', 'PATCH'])
def product(product_id):
    index = -1
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == product_id:
            index = i
            break
    if index == -1:
        return '{ "message": "not found"}', status.HTTP_404_NOT_FOUND
    if request.method == 'GET':
        return jsonify(PRODUCTS[index])
    elif request.method == 'DELETE':
        del PRODUCTS[index]
        return '', status.HTTP_204_NO_CONTENT
    elif request.method == 'PATCH':
        data = request.get_json()
        if data['name'] == '':
            return '', 422
        PRODUCTS[index] = {
            'id': PRODUCTS[index]['id'],
            'name': data['name'],
        }
        return jsonify(PRODUCTS[index]), status.HTTP_201_CREATED
        #status.HTTP_204_NO_CONTENT