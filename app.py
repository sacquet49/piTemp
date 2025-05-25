import adafruit_dht
import board
import time
import atexit
from flask import Flask, render_template, jsonify

# GPIO 4
dhtDevice = adafruit_dht.DHT11(board.D4)
app = Flask(__name__)
temperature_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    try:
        temperature = dhtDevice.temperature
        if temperature is not None:
            temperature_data.append((time.time(), temperature))
            if len(temperature_data) > 50:
                temperature_data.pop(0)
        return jsonify(temperature_data)
    except Exception as e:
        print("Erreur capteur :", e)
        return jsonify(temperature_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

atexit.register(dhtDevice.exit)
