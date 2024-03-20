import requests


r = requests.get("https://httpbin.org/basic-auth/uzytkownik/haslo",auth=("uzytkownik","haslo"))

print(r.json())

r = requests.get("https://httpbin.org/ip")

print(r.json())