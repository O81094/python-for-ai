import requests


def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data["current"]["temperature_2m"]

get_weather(40.7128, -74.0060)

print(f"Parris Temprature: {get_weather(33.75, -84.39)}")

