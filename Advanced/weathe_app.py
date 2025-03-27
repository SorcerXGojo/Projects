import requests 
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
if api_key is None:
    print("Error: WEATHER_API_KEY environment variable not set.")
    exit()

city_name = input("Enter city name: ")

  
    # Build the API URL
base_url = "https://api.openweathermap.org/data/2.5/weather?"
url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    # Make the API request
response = requests.get(url)

if response.status_code != 200:
    print("Error: API request unsuccessful.")
    exit()
elif response.status_code == 200:
    data = response.json()
# Extract and print relevant weather information
    print("Weather in", data['name'], ":")
    print("Description:", data['weather'][0]['description'])
    print("Temperature:", data['main']['temp'], "°C")
    print("Humidity:", data['main']['humidity'], "%")
    print("Wind speed:", data['wind']['speed'], "m/s")
else:
    print("Error:", response.status_code, response.text)
    