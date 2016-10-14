from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	resp = twilio.twiml.Response()
	resp.say("This will eventually become Julian Alerts. Please stay tuned for updates.")

	return str(resp)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
