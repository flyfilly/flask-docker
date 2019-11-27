import os

from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

port = int(os.getenv("PORT", 5555))


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({
        "message": "hello, world"
    }), HTTPStatus.OK


@app.errorhandler(405)
def not_allowed(e):
    return "", HTTPStatus.METHOD_NOT_ALLOWED


@app.errorhandler(404)
def not_found(e):
    return "", HTTPStatus.NOT_FOUND


@app.errorhandler(500)
def server_error(e):
    return str(e), HTTPStatus.INTERNAL_SERVER_ERROR


if __name__ == '__main__':
    app.run(
        port=port
    )
