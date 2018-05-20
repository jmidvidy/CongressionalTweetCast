# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, Response, request, redirect, url_for, jsonify


app = Flask(__name__)



@app.route("/C:/Users/jmidv/Documents/Spring 2018/EECS 338/backend/ajax_caller.py", methods=['POST'])
def ajax_caller():
	return jsonify({"Classification" : "Classification!!!!!"})



if __name__ == '__main__':
	app.run(debug=True)





