from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "có cái đầu buồi liên hệ dailygame1111 de mua"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)