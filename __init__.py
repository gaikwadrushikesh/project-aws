from flask import Flask, jsonify, Request

app = Flask(__name__)

@app.route("/test")
def test():
    return "Hello"

if __name__ == "__main__":
    app.run()