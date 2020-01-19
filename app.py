from products import products
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's List"})


@app.route('/product/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name]
    if(len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})
    # return jsonify(product_name)


@app.route('/product', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quentity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product added succesfully", "product": products})


@app.route('/product/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [
        product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name'],
        productFound[0]['price'] = request.json['price'],
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({"message": "Product Updated",
                        "product": productFound[0]})
    return jsonify({"message": "Product Not Found"})


@app.route('/product/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [
        product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({"message": "Product Deleted",
                        "products": products})
    return jsonify({"message": "Product Not Found"})

    # if len(productFound) > 0:
    #     products.remove(productFound)
    #     return jsonify({"message": "Product Deleted",
    #                     "products": products})
    # return jsonify({"message": "Product Not Found"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
