  Weather Data Fetcher

This project provides a Python-based utility which fetches weather data for specified locations using the OpenWeatherMap API and save it in JSON format. It also provides functionality to parse the JSON data into a CSV file for easy analysis.

   Features:

- Fetches real-time weather data for multiple locations.
- Saves weather data in a JSON file.
- Converts the JSON file into CSV format.

Requirements:

- Python 3.12 or above.
- The following Python libraries: requests,json,csv,os.
- Pip installation
- An OpenWeatherMap API key. You can get one by signing up at [OpenWeatherMap](https://openweathermap.org/api).

Configuration:
  
1. Set up the OpenWeatherMap API key as an environment variable named `OPENWEATHER_API_KEY`:"a7e7f5287a69c6d3ae045210b3d6bb41"
  
2. Modify the `LOCATIONS` variable in the script to include the cities we want to fetch weather data for:

      LOCATIONS = ["London", "New York", "Dubai"]
 
4. Specify the desired output units (`metric`, `imperial`, or `standard`) by modifying the `UNITS` variable:

   UNITS = "metric" or "imperial" or standard

 Usage:
 
1. Run the script to fetch weather data into Json file.
2.  Now convert Json file into CSV File,excluding the weather array.
3. Check the output files:
   - JSON file: Contains raw weather data for all specified locations.
   - CSV file: Contains a tabular representation of key weather data fields.

 Output File Details:
 
- `JSON_weather.json`: Stores the fetched weather data in JSON format.
- `CSV_weather.csv`: Contains parsed weather data, including:
  - **City**: The name of the location.
  - **Temperature**: Current temperature in the specified units.
  - **Humidity**: Current humidity percentage.
  - **Weather Description**: A short description of the weather.

Example:
JSON Output
json
[
    {
        "name": "London",
        "main": {
            "temp": 15.0,
            "humidity": 82
        },
        "weather": [
            {
                "description": "light rain"
            }
        ]
    }
]

CSV Output:

City,Temperature,Humidity,Weather Description
London,15.0,82,light rain

Notes:

- Ensure the API key is valid to avoid authentication errors.
- Handle exceptions and errors, such as failed API requests, for production use.




Created by Neelimatula
