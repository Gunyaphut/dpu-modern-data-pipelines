import requests


API_KEY = "5220f3589824c88456c8a7bf8fb5832f"
payload = {
    "q": "bangkok",
    "appid": API_KEY,
    "units": "metric"
}
url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params=payload)
print(response.url)

data = response.json()
print(data)