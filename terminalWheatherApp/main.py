import requests

location = "Kostinbrod,BG"
api_key = "d0291172d4d64dc7d7f763e042391f49"

url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

response = requests.get(url)
weather_data = response.json()

if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data['main']['temp'] - 273.15
    print(f"Temperature: {temperature:.2f} °C")
else:
    print(f"Request failed with status code: {response.status_code}")

