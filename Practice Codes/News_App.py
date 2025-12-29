import requests

url = "https://gnews.io/api/v4/search?q=example&apikey=API_KEY"

params = {
    "q": "india",
    "lang": "en",
    "country": "in",
    "max": 5,
    "apikey": "4186e3d7433060de6c06d3d766ae02ef"   # 👈 YAHAN API KEY
}

response = requests.get(url, params=params)
data = response.json()

for news in data["articles"]:
    print(news["Title"])
# print(data)