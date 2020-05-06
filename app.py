import os

from flask import Flask
from flask import jsonify

import praw

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"message": "Goodbye world!"})


@app.route('/test', methods=["GET"])
def test():

    print(os.getenv("CLIENT_ID"))
    print(os.getenv("CLIENT_SECRET"))
    print(os.getenv("USER_AGENT"))


    reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                         client_secret=os.getenv("CLIENT_SECRET"),
                         user_agent=os.getenv("USER_AGENT"),
                         username=os.getenv("USERNAME"),
                         password=os.getenv("PASSWORD"))

    return jsonify({"message":"this is a test endpoint."})



if __name__ == "__main__":
    app.run(debug=True)




# https://www.reddit.com/api/me.json
# https://www.reddit.com/r/randnsfw/top.json?limit=50