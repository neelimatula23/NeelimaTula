import requests
import json
import csv
import os

def fetch_weather_data(api_key, locations, units="metric", output_filename="weather_data.json"):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_data = []

    for location in locations:
        params = {"q": location, "appid": api_key, "units": units}
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data.append(response.json())

    with open(output_filename, 'w') as json_file:
        json.dump(weather_data, json_file, indent=4)

    return weather_data

def parse_json_to_csv(input_filename, output_filename):
    with open(input_filename, 'r') as json_file:
        weather_data = json.load(json_file)

    headers = ["City", "Temperature", "Humidity", "Weather Description"]

    with open(output_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for data in weather_data:
            writer.writerow([
                data["name"],
                data["main"]["temp"],
                data["main"]["humidity"],
                data["weather"][0]["description"]
            ])

if __name__ == "__main__":
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "a7e7f5287a69c6d3ae045210b3d6bb41")
    LOCATIONS = ["London", "New York"]
    UNITS = "metric"
    JSON_FILE = "JSON_weather.json"
    CSV_FILE = "CSV_weather.csv"

    weather_data = fetch_weather_data(API_KEY, LOCATIONS, UNITS, JSON_FILE)
    parse_json_to_csv(JSON_FILE, CSV_FILE)