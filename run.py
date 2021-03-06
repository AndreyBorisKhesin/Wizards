from flask import Flask, request, redirect
import time
import twilio.twiml
import sys
sys.path.append("C:\\Users\\Andrey\\Documents\\Wizards\\Project")
from response import Response

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.message(Response.generateresponse(
    	request.values.get('From', None),
	request.values.get('Body', None),
	request.values.get('FromCity', None),
	time.time()))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
