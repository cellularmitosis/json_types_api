#!/usr/bin/env python

from flask import Flask, Response
import json

app = Flask(__name__)

def json_response(data):
	return Response(
		response=json.dumps(data),
		status=200,
		mimetype="application/json"
	)

@app.route("/")
def root():
	return """
<html>
<body>
<ul>
<li><a href="/null">JSON null</a></li>
<li><a href="/number">JSON number</a></li>
<li><a href="/string">JSON string</a></li>
<li><a href="/boolean">JSON boolean</a></li>
<li><a href="/array">JSON array</a></li>
<li><a href="/object">JSON object</a></li>
</ul>
</body>
</html>
"""

@app.route("/null")
def json_null():
	return json_response(None)

@app.route("/number")
def json_number():
	return json_response(3.14159)

@app.route("/string")
def json_string():
	return json_response("Hello, world!")

@app.route("/boolean")
def json_boolean():
	return json_response(True)

@app.route("/array")
def json_array():
	return json_response([2,3,5,7,11,13,17])

@app.route("/object")
def json_object():
	return json_response({"one": 1, "two": 2, "three": 3})

if __name__ == "__main__":
    app.run()
