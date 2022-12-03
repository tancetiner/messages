from flask import Flask, request, render_template_string, abort
from Message import *
import os

app = Flask(__name__)

messageClass = Message()


@app.route("/", methods=["GET"])
def homepage():
    return "<h1>HOMEPAGE</h1>"


@app.route("/messages", methods=["POST"])
def putMessage():
    data = request.get_json()
    if not (data and data["message"] != ""):
        return {"Error": "No message data detected!"}
    message = data["message"]
    return messageClass.putMessage(message)


@app.route("/messages/<hash>", methods=["GET"])
def getMessage(hash):
    return messageClass.getMessage(hash)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
