import requests
from dotenv import load_dotenv
from emailer import send_email
import os

# load the environment variables from the .env file
load_dotenv()


def fetch_temperature(location: str):
    print(f"Fetching Weather data for location {location}")
    api_key = os.environ['API_WEATHER']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32

        return {
            "temperature_celsius": f"{temperature_celsius:.2f}",
            "temperature_fahrenheit": f"{temperature_fahrenheit:.2f}"
        }

    return


def send_alert(email: str, message: str) -> None:
    send_email('Temperature Alert!', message, email, os.environ['TEST_EMAIL'],
               os.environ['TEST_EMAIL_PASSWORD'])
    return
