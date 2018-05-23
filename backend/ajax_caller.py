#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_cors import CORS
import model_test 

app = Flask(__name__)
CORS(app)

@app.route("/ajax_caller", methods=['POST'])
def ajax_caller():
    twitter_handle = request.form.get("twitter_handle")
    election = request.form.get("election")
    cl = model_test.classify(election, twitter_handle)
    classification = cl[0]
    hw = cl[1]
    return jsonify({"result" : classification, "hotwords": hw})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)






