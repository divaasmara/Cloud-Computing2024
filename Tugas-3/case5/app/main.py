import os
import requests
from datetime import datetime
from flask import Flask, render_template, request
import pycountry
from dotenv import load_dotenv
import socket

app = Flask(__name__)
load_dotenv()

weather_data = {}


def name_to_cord(location):
    """
    receive user input from form_page
    sends the reacived long and lat to cord_to_weather which returns the actual weather data
    returns the response
    """
    res = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={os.getenv("key")}').json()
    if not res or 'cod' in res:
        return False

    weather_data['lat'] = res[0]["lat"]
    weather_data['lon'] = res[0]["lon"]
    weather_data['name'] = res[0]["name"]
    weather_data['country'] = pycountry.countries.get(alpha_2=res[0]["country"]).name
    return True


def cord_to_weather(lat, lon):
    """
    reacives cords from name_to_cord and returns the actual weather response
    """
    res = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}"
                       f"&exclude=hourly,minutely,current&units=metric&appid={os.getenv('key')}").json()
    weather_data['daily'] = res['daily'][1:8]


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

    for item in weather_data['daily']:
        for key, val in item.items():
            if key == 'dt':
                item['dt'] = datetime.fromtimestamp(item['dt']).date()
    return render_template("weather.html", name=weather_data["name"], latitude=weather_data['lat'],
                           longitude=weather_data['lon'], country=weather_data['country'], daily=weather_data['daily'], error=False, host=socket.gethostname())


if __name__ == "__main__":
    app.run(host="0.0.0.0")

