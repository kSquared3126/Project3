from logging import debug
from flask import Flask, render_template, jsonify
import numpy as np
import requests

app = Flask(__name__)

GPIO.setmode(GPIO.BCM) # Choose BCM to use GPIO numbers instead of pin numbers
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)
GPIO.input(17, GPIO.LOW)

@app.route('/testcall', methods={'POST'})
    def updateCall():
        rand_num = np.random.rand(1)

        return jsonify(' ', render_template, )

@app.route("/")
def index():
    senPIRSts=GPIO.input(17)
    templateData = {
        'SensorData': senPIRSts,
        'title': 'HELLO!',
        'x': 10
    }


	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)


