from flask import Flask,jsonify

app = Flask(__name__)
from products import products


@app.route('/ping')
def ping():
    return jsonify({"message":"pong"})
@app.route('/products')
def getProducts():
    return jsonify ({
        "message":"Product's list",
        "products":products
        })
@app.route('/products/<product_name>')
def getProduct(product_name):
    productsFound = [product for product in  products if product['name']==product_name]
    if (len(productsFound)> 0):
        return jsonify({"Products":productsFound[0]})
    return jsonify ({"message":"Product not found"})
if __name__=="__main__":
    app.run(debug=True,port=4000)