from flask import Flask, render_template, request, jsonify

from facebook import get_account_types as fb_types
from facebook import get_facebook_questions, run_facebook

from instagram import get_account_types as ig_types
from instagram import get_instagram_questions, run_instagram

from whatsapp import get_account_types as wa_types
from whatsapp import get_whatsapp_questions, run_whatsapp

from password_strength import check_password_strength
from password_generator import generate_passphrase
from password_breach import check_password_breach


app = Flask(__name__)


# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Report page (full multi-account report)
@app.route("/report")
def report():
    return render_template("report.html")


# Get account types for selected platform
@app.route("/account_types/<platform>")
def account_types(platform):
    if platform == "facebook":
        return jsonify(fb_types())
    elif platform == "instagram":
        return jsonify(ig_types())
    elif platform == "whatsapp":
        return jsonify(wa_types())
    return jsonify({})


# Get questions based on platform + account type
@app.route("/questions/<platform>/<account_type>")
def questions(platform, account_type):
    if platform == "facebook":
        return jsonify(get_facebook_questions(account_type))
    elif platform == "instagram":
        return jsonify(get_instagram_questions(account_type))
    elif platform == "whatsapp":
        return jsonify(get_whatsapp_questions(account_type))
    return jsonify([])


# Run assessment
@app.route("/run_assessment", methods=["POST"])
def run_assessment():
    data = request.json
    platform = data.get("platform")
    account_type = data.get("account_type")
    answers = data.get("answers")

    if platform == "facebook":
        score, risk, recommendations = run_facebook(account_type, answers)
    elif platform == "instagram":
        score, risk, recommendations = run_instagram(account_type, answers)
    elif platform == "whatsapp":
        score, risk, recommendations = run_whatsapp(account_type, answers)
    else:
        return jsonify({"error": "Invalid platform"}), 400

    return jsonify({
        "score": score,
        "risk_level": risk,
        "recommendations": recommendations
    })


# ── Password Tools ─────────────────────────────────────────────────────────────

@app.route("/check_strength", methods=["POST"])
def check_strength():
    data = request.json
    password = data.get("password", "")
    result = check_password_strength(password)
    return jsonify(result)


@app.route("/generate_passphrase", methods=["POST"])
def generate():
    data = request.json or {}
    num_words = int(data.get("num_words", 5))
    num_words = max(4, min(num_words, 8))  # clamp between 4 and 8
    result = generate_passphrase(num_words=num_words)
    return jsonify(result)


@app.route("/check_breach", methods=["POST"])
def check_breach():
    data = request.json
    password = data.get("password", "")
    result = check_password_breach(password)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
