from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "fooddb")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")

def get_conn():
    return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

@app.route("/order", methods=["POST"])
def order():
    data = request.json
    dish = data.get("dish")
    user = data.get("user")
    if not dish or not user:
        return jsonify({"error": "Invalid input"}), 400
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (dish, username) VALUES (%s, %s)", (dish, user))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Notification: {user} ordered {dish}")
    return jsonify({"message": f"Order received for {dish} by {user}"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

