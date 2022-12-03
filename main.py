from flask import (
    Flask,
    request,
    render_template_string,
    render_template,
    jsonify,
    abort,
)
from Message import *
import os

app = Flask(__name__)

messageClass = Message()


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


@app.route("/messages", methods=["POST"])
def putMessage():
    data = request.get_json()
    if not (data and data["message"] != ""):
        abort(404, description="No message data detected!")
        # return {"Error": "No message data detected!"}
    message = data["message"]
    return messageClass.putMessage(message)


@app.route("/messages/<hash>", methods=["GET"])
def getMessage(hash):
    response = messageClass.getMessage(hash)
    if response == -1:
        abort(404, description="Message not found with given hash!")
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
