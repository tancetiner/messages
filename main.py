from flask import Flask, request, render_template_string, abort
from Message import *

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


# @app.errorhandler(404)
# def page_not_found(e):
#     return (
#         render_template_string(
#             "Message not found with given hash! Error: {{ errorCode }}", errorCode="404"
#         ),
#         404,
#     )


# if __name__ == "__main__":
#     app.debug = False
#     app.run()
