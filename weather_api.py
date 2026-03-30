import requests
api_key = "8e6ef8175a1f409b87465510262603"
city='chennai'
use=
response=requests.get(url)
date=response.json()
temperature=date["main"]["temp"]
weather=date["weather"][0]["desciples"]
print("city:",city)
print("temperature:",temperature)
print("humidity:",humidity)
print("weather:",weather)