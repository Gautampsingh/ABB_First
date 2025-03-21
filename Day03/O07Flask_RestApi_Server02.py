
import json

from flask import Flask
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

api.add_resource(Products, "/getproduct/<string:product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
