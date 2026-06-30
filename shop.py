from flask import Flask

app = Flask(__name__)
products = [
    {"name": "laptop", "price": 500},
    {"name": "phone", "price": 250},
    {"name": "headphones", "price": 1000}
]

@app.route("/")
def home():
    html = """
    <h1> divine shopping website</h1>
    """

    for product in products:
        html += f"""
        <hr>
        <h2>{product['name']}</h2>
        <p>price: $
{product['price']}</p>
       <button>add to cart</button>

        """      

    if __name__ == "__main__":
        app.run(debug=True)   