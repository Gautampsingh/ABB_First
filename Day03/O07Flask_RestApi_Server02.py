
import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'Pepsi' : {'item': '2 ltr Bottle', 'price': 120, 'qty': 150},
    'Coke' : {'item': '500 ml Bottle', 'price': 60, 'qty': 225},
    'Thumbs_up': {'item': '300 ml CAN', 'price': 75, 'qty': 80}
}

class Products(Resource):

    def get(self, product):
        return {product : products[product]}


    def put(self, product):
        products[product]['cat'] = request.form['cat']
        return {product :products[product]}

    def patch(self, product):
        data1 = request.json
        data = json.loads(data1)
        products[product][list(data.keys())[0]] = data[list(data.keys())[0]]
        return {product :products[product]}

    def post(self, product):
        data1 = request.json
        data = json.loads(data1)
        products[product] = data
        return products

    def delete(self, product):
        if product in products:
            del products[product]
            return products
        else:
            print(product)
            print(products)
            print(product in products[product])
            return {'KeyError': "Invalid Key, Please enter a valid key....."}


api.add_resource(Products, "/getproduct/<string:product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
