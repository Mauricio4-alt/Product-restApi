from flask import Flask

app = Flask(__name__)
from products import products
if __name__=="__main__":
    app.run(debug=True,port=4000)