  Weather Data Fetcher

This project provides a Python-based utility to fetch weather data for specified locations using the OpenWeatherMap API and save it in both JSON and CSV formats.

   Features

- Fetches real-time weather data for multiple locations.
- Saves weather data in a JSON file.
- Converts the JSON data into a  CSV format.

  Requirements

- Python 
- The following Python libraries: requests,json,csv,os
- Google Colab environment.

  Setup Instructions for Google Colab

1. Open Google Colab : Go to Google Colab.
2. Install Dependencies :  ensure all required libraries are installed
3. Import the Script : Copy the script code into a cell in your Colab notebook and execute the cell.
4. Set API Key : You can directly set the API_KEY variable in the script or use Colab's environment variables
   import os
   os.environ["OPENWEATHER_API_KEY"] = "your_api_key_here"
5. Run the Script : Run the script cell. The outputs, JSON_weather.json and CSV_weather.csv, will be saved in the Colab environment.
6. Download the Files : To download the generated files to your local machine, use the following code
    from google.colab import files
    files.download("JSON_weather.json")
    files.download("CSV_weather.csv")

 Configuration

You can modify the following variables in the script to customize the behavior:
- API_KEY: Your OpenWeatherMap API key.
- LOCATIONS: A list of cities for which weather data will be fetched.
- UNITS: Measurement units (default: metric for Celsius).
- JSON_FILE: Name of the JSON file for saving fetched weather data.
- CSV_FILE: Name of the CSV file for saving parsed weather data.

   Functions

1. fetch_weather_data(api_key, locations, units="metric", output_filename="weather_data.json")
        - Fetches weather data for the specified locations.
Parameters:
* api_key: OpenWeatherMap API key.
* locations: List of city names.
* units: Measurement units (e.g., metric, imperial).
* output_filename: Name of the JSON file to save the data.
* Returns: Weather data as a Python list.

2. parse_json_to_csv(input_filename, output_filename)
       -Converts weather data from a JSON file into a CSV file.
Parameters:
* input_filename: Name of the JSON file with weather data.
* output_filename: Name of the CSV file to save parsed data.

   Example Output

JSON File (JSON_weather.json):
[
    {
        "name": "London",
        "main": {
            "temp": 15.5,
            "humidity": 82
        },
        "weather": [
           {
                "description": "light rain"
            }
        ]
    }
]

CSV File (CSV_weather.csv):

City,Temperature,Humidity,Weather Description
London,15.5,82,light rain
New York,18.3,65,clear sky
India,29.4,78,scattered clouds

   Error Handling

- If a location is not found or the API key is invalid, the script skips the location without crashing.

  Created by Neelima Tula
