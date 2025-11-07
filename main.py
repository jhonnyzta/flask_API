from flask import Flask
import json
import os

app = Flask(__name__)

with open("data.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

@app.route("/")
def home():
    return "hola"

@app.route("/get/<item_id>", methods=["GET"])
def get_item(item_id):
    item = DATA.get(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Not fund"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
