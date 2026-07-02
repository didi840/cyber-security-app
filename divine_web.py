from flask import Flask, render_template, request, url_for, make_response
import time

app = Flask(__name__)


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
    return (
        "DIVINE ASUOMA SYSTEM DICTATE REPORT\n"
        "====================================\n"
        f"System version 11: {system}\n"
        f"System updated: {update}\n"
        f"Brand: {brand}\n"
        f"Shared system: {shared}\n"
        f"Involved in fraud: {fraud}\n"
        f"Previously hacked: {hacking}\n"
        f"Score: {score}/60\n"
        f"Threat level: {level}\n"
        f"Rating: {rating}\n"
        f"System status: {status}\n"
        "====================================\n"
        + (
            "Your system is in very good condition.\n"
            if score >= 50
            else "Your system is reasonably safe, but review the areas marked.\n"
            if score >= 35
            else "Your system may be at risk. Please improve security settings.\n"
        )
    )


@app.route("/", methods=["GET", "POST"])
def index():
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
