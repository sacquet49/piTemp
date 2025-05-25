import Adafruit_DHT
import time
from flask import Flask, render_template, jsonify

sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO 4

app = Flask(__name__)
temperature_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if temperature is not None:
        temperature_data.append((time.time(), temperature))
        # Ne garde que les dernières 50 valeurs
        if len(temperature_data) > 50:
            temperature_data.pop(0)
    return jsonify(temperature_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
