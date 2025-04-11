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
@app.route('/products/<name>')
def getProduct(name):
    return jsonify ({
        "message":"Products found",
        "product":[products[i] for i in range(len(products)) if products[i]["name"] == name ]
        })
if __name__=="__main__":
    app.run(debug=True,port=4000)