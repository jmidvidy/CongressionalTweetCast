#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_cors import CORS
import model_test 
import pull_tweets

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def ajax_caller():
    
    #instantiate
    classification = "e"
    hw = "e"
    
    #collect inputs
    twitter_handle = request.form.get("twitter_handle")
    election = request.form.get("election")
    
    
    #get rid of first character
    a = twitter_handle[:1]
    if a == '@':
        twitter_handle = twitter_handle[1:]
    
    #call pull_tweets to pull user tweets
    p = pull_tweets.pull(twitter_handle)
    if p == 0:
        invalid = "protected" #invalid means user is either protected
        return jsonify({"result" : classification, "hotwords": hw, "invalid" : invalid})
    elif p == 2:
        invalid = "invalid_handle"
        return jsonify({"result" : classification, "hotwords": hw, "invalid" : invalid})
    else:
        invalid = "False"
    
    #call model_test to classify the model and get hot-words
    cl = model_test.classify(election, twitter_handle)
    classification = cl[0]
    hw = cl[1]
    
    return jsonify({"result" : classification, "hotwords": hw, "invalid" : invalid})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)






