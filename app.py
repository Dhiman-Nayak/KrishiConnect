from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to fetch temperature data
def fetch_temperature():
    try:
        response = requests.get('http://192.168.95.93/temperature')
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
    return "N/A"  # Return a default value if data cannot be fetched

def fetch_humidity():
    try:
        response = requests.get('http://192.168.95.93/humidity')
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
    return "N/A"  # Return a default value if data cannot be fetched

def fetch_ldr():
    try:
        response = requests.get('http://192.168.95.93/ldr')
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
    return "N/A"  # Return a default value if data cannot be fetched

def fetch_soil():
    try:
        response = requests.get('http://192.168.95.93/soil-mois')
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
    return "N/A"  # Return a default value if data cannot be fetched

def fetch_rain():
    try:
        response = requests.get('http://192.168.95.93/rain')
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
    return "N/A"  # Return a default value if data cannot be fetched

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ldr')
def ldr():
    ldr = fetch_ldr()
    return ldr

@app.route('/temp')
def temp():
    temp = fetch_temperature()
    return temp

@app.route('/humidity')
def hum():
    hum = fetch_humidity()
    return hum

@app.route('/soil')
def soil():
    soil = fetch_soil()
    return soil

@app.route('/rain')
def rain():
    rain = fetch_rain()
    return rain



if __name__ == '__main__':
    app.run(debug=True)