import requests
from dotenv import load_dotenv
import os

# load the environment variables from the .env file
load_dotenv()


def fetch_temperature(location: str):
    api_key = os.environ['API_WEATHER']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32
        
        return {
            "temperature_celsius": f"{temperature_celsius:.2f}",
            "temperature_fahrenheit": f"{temperature_fahrenheit:.2f}"
        }
    else:
        return None

def send_alert(message: str):
    # Implement the code to send an alert/notification to the user
    # Replace this with your actual implementation
    print(f"Alert: {message}")