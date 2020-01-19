from products import products
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's List"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
