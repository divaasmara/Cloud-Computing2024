import os
import requests
from datetime import datetime
from flask import Flask, render_template, request
import pycountry
import socket

app = Flask(__name__)

weather_data = {}

# API key 
API_KEY = "876c721a9fef471b9e0175307242212"


def name_to_cord(location):
    """
    Mendapatkan koordinat lokasi menggunakan WeatherAPI.
    """
    res = requests.get(
        f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={location}"
    ).json()

    if not res or isinstance(res, dict) and 'error' in res:
        return False

    weather_data['lat'] = res[0]["lat"]
    weather_data['lon'] = res[0]["lon"]
    weather_data['name'] = res[0]["name"]
    weather_data['country'] = res[0]["country"]
    return True


def cord_to_weather(lat, lon):
    """
    Mendapatkan cuaca harian berdasarkan koordinat menggunakan WeatherAPI.
    """
    res = requests.get(
        f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={lat},{lon}&days=7"
    ).json()

    if "forecast" in res:
        weather_data['daily'] = [
            {
                'dt': forecast['date'],
                'temp_min': forecast['day']['mintemp_c'],
                'temp_max': forecast['day']['maxtemp_c'],
                'condition': forecast['day']['condition']['text'],
                'icon': forecast['day']['condition']['icon']
            }
            for forecast in res['forecast']['forecastday']
        ]


@app.route("/", methods=['GET'])
def form_page():
    return render_template("weather.html", host=socket.gethostname())


@app.route("/", methods=['POST'])
def weather():
    form = request.form
    invalid_input = name_to_cord(form['location'])
    if not invalid_input:
        return render_template("weather.html", error=True)

    cord_to_weather(weather_data['lat'], weather_data['lon'])

    return render_template(
        "weather.html",
        name=weather_data["name"],
        latitude=weather_data['lat'],
        longitude=weather_data['lon'],
        country=weather_data['country'],
        daily=weather_data['daily'],
        error=False,
        host=socket.gethostname()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
