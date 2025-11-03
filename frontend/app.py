from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:5000/order")

dishes = [
    {"name": "Masala Dosa", "image": "dosa.jpg"},
    {"name": "Soft Idli", "image": "idli.jpg"},
    {"name": "Medu Vada", "image": "vada.jpg"},
    {"name": "Sambar", "image": "sambar.jpg"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        user = request.form.get("user")
        dish = request.form.get("dish")
        if user and dish:
            res = requests.post(BACKEND_URL, json={"user": user, "dish": dish})
            message = res.json().get("message", "Order sent")
    return render_template("index.html", dishes=dishes, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

