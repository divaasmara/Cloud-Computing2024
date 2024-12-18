import requests
import mysql.connector
import time

API_KEY = 'your_openweathermap_api_key'
CITY = 'YourCity'
DB_CONFIG = {
    'host': 'db',
    'user': 'root',
    'password': 'example',
    'database': 'weather_data'
}


def fetch_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data


def save_weather(data):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    query = (
        "INSERT INTO weather (city, temperature, description, timestamp) "
        "VALUES (%s, %s, %s, %s)"
    )
    cursor.execute(query, (
        data['name'],
        data['main']['temp'],
        data['weather'][0]['description'],
        time.strftime('%Y-%m-%d %H:%M:%S')
    ))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    while True:
        weather_data = fetch_weather()
        save_weather(weather_data)
        time.sleep(1800)  # Ambil data setiap 30 menit
