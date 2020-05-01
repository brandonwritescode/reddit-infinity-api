from flask import jsonify


def index():
    return jsonify({"message": "this is the home route"})


def test():
    return jsonify({"message": "this is a test"})

