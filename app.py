from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"message": "Goodbye world!"})


if __name__ == "__main__":
    app.run(debug=True)
