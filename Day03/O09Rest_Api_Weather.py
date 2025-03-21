
import requests
import json


def get_current_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {'appid': api_key, "q": city_name, 'units': 'metric'}

    try:
        response = requests.get(base_url, params = params)
        response.raise_for_status()

        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except json.JSONDecoder:
        print("Failed to decode JSON response....")
        return None

api_key = "cdc0f4bc47cea27cec3b245bdad9a5eb"
city_name = "Bengaluru"
weather_data = get_current_weather(api_key, city_name)

if weather_data:
    print(json.dumps(weather_data, indent=4))