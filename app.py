from flask import Flask, render_template, redirect, url_for, session, request, flash

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-key"

products = [
    {
        "id": 1,
        "name": "Classic Shirt",
        "price": 29.99,
        "description": "Comfortable everyday shirt for work or weekend.",
    },
    {
        "id": 2,
        "name": "Sneaker Shoes",
        "price": 59.99,
        "description": "Lightweight sneakers for daily walking and running.",
    },
    {
        "id": 3,
        "name": "Jeans",
        "price": 49.99,
        "description": "Modern fit denim jeans with a soft stretch.",
    },
    {
        "id": 4,
        "name": "Leather Wallet",
        "price": 19.99,
        "description": "Slim wallet with multiple card slots and cash pocket.",
    },
]


def get_cart():
    return session.setdefault("cart", {})


def cart_total(cart):
    total = 0.0
    for product_id, quantity in cart.items():
        product = next((p for p in products if p["id"] == int(product_id)), None)
        if product:
            total += product["price"] * quantity
    return total


@app.route("/")
def index():
    cart = get_cart()
    count = sum(cart.values())
    return render_template("index.html", products=products, cart_count=count)


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    cart = get_cart()
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart
    flash("Added item to cart.")
    return redirect(url_for("index"))


@app.route("/cart")
def view_cart():
    cart = get_cart()
    items = []
    for product_id, quantity in cart.items():
        product = next((p for p in products if p["id"] == int(product_id)), None)
        if product:
            items.append({"product": product, "quantity": quantity})
    total = cart_total(cart)
    return render_template("cart.html", items=items, total=total)


@app.route("/remove/<int:product_id>")
def remove_from_cart(product_id):
    cart = get_cart()
    cart.pop(str(product_id), None)
    session["cart"] = cart
    flash("Removed item from cart.")
    return redirect(url_for("view_cart"))


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = get_cart()
    if not cart:
        flash("Your cart is empty.")
        return redirect(url_for("index"))

    if request.method == "POST":
        session["cart"] = {}
        flash("Order placed successfully! Thank you for shopping.")
        return redirect(url_for("index"))

    items = []
    for product_id, quantity in cart.items():
        product = next((p for p in products if p["id"] == int(product_id)), None)
        if product:
            items.append({"product": product, "quantity": quantity})

    total = cart_total(cart)
    return render_template("checkout.html", items=items, total=total)


if __name__ == "__main__":
    app.run(debug=True)
