import requests

url = "https://gnews.io/api/v4/search?q=example&apikey=API_KEY"
usr = ""

params = {
    "q": "Stock market",
    "lang": "en",
    "country": "in",
    "max": 5,
    "apikey": "4186e3d7433060de6c06d3d766ae02ef"   #YAHAN API KEY
}

print("Hello And Welcome To Aaj Tak \n ")
print("1.General News \n 2.World \n 3. Business \n 4.Technology \n 5.Nation \n 6.Entertainment \n 7.Sports \n 8.Science \n 9.Health \n 10. Exit()  ")



usr = input("Enter The Topic Name  To Search The News ")
params["q"] = usr # 

if usr == "Exit" or usr == "exit":
    exit()
else:
    response = requests.get(url, params=params)
    data = response.json()
    for news in data["articles"]:
     print(news["title"])


# print(data)