from flask import Flask, render_template, redirect, url_for, session, request, flash, make_response
import time

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


def evaluate_score(system, update, brand, shared, fraud, hacking):
    score = 0
    score += 10 if system == "yes" else 0
    score += 10 if update == "yes" else 0
    score += 10 if brand == "macbook" else 0
    score += 10 if shared == "no" else 0
    score += 10 if fraud == "no" else 0
    score += 10 if hacking == "no" else 0
    return score


def threat_level(score):
    if score >= 50:
        return "LOW", "EXCELLENT", "SECURE"
    if score >= 35:
        return "MEDIUM", "GOOD", "STABLE"
    return "HIGH", "AT RISK", "UNSAFE"


def build_report(system, update, brand, shared, fraud, hacking, score, level, rating, status):
    lines = [
        "DIVINE ASUOMA SYSTEM DICTATE REPORT",
        "====================================",
        f"System version 11: {system}",
        f"System updated: {update}",
        f"Brand: {brand}",
        f"Shared system: {shared}",
        f"Involved in fraud: {fraud}",
        f"Previously hacked: {hacking}",
        f"Score: {score}/60",
        f"Threat level: {level}",
        f"Rating: {rating}",
        f"System status: {status}",
        "====================================",
    ]
    if score >= 50:
        lines.append("Your system is in very good condition.")
    elif score >= 35:
        lines.append("Your system is reasonably safe, but review the areas marked.")
    else:
        lines.append("Your system may be at risk. Please improve security settings.")
    return "\n".join(lines)


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


@app.route("/scanner", methods=["GET", "POST"])
def scanner():
    if request.method == "POST":
        system = request.form.get("system", "no")
        update = request.form.get("update", "no")
        brand = request.form.get("brand", "windows")
        shared = request.form.get("shared", "yes")
        fraud = request.form.get("fraud", "yes")
        hacking = request.form.get("hacking", "yes")

        score = evaluate_score(system, update, brand, shared, fraud, hacking)
        level, rating, status = threat_level(score)
        report_text = build_report(system, update, brand, shared, fraud, hacking, score, level, rating, status)

        download_url = url_for(
            "download_report",
            system=system,
            update=update,
            brand=brand,
            shared=shared,
            fraud=fraud,
            hacking=hacking,
        )

        return render_template(
            "divine_report.html",
            system=system,
            update=update,
            brand=brand,
            shared=shared,
            fraud=fraud,
            hacking=hacking,
            score=score,
            level=level,
            rating=rating,
            status=status,
            report_text=report_text,
            download_url=download_url,
        )

    return render_template("divine_form.html")


@app.route("/download")
def download_report():
    system = request.args.get("system", "no")
    update = request.args.get("update", "no")
    brand = request.args.get("brand", "windows")
    shared = request.args.get("shared", "yes")
    fraud = request.args.get("fraud", "yes")
    hacking = request.args.get("hacking", "yes")

    score = evaluate_score(system, update, brand, shared, fraud, hacking)
    level, rating, status = threat_level(score)
    report_text = build_report(system, update, brand, shared, fraud, hacking, score, level, rating, status)

    filename = f"divine_report_{time.strftime('%Y%m%d_%H%M%S')}.txt"
    response = make_response(report_text)
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response


if __name__ == "__main__":
    app.run(debug=True)
