import amino
import time
import json
prox = {
    "http": "61.29.96.146:80",
    "https": "51.158.68.68:8761",
}
with open("info.json", "r") as info:
    data = json.load(info)
    SID = data["sid"]
    EMAIL = data["email"]
    PASS = data["password"]
    comId = data["community"]
client = amino.Client(proxies=prox)
res = client.login(email= EMAIL,password= PASS)
print("bot Logged in successfully")
my_id = client.userId
i = 0
while True:
    users = client.get_all_users(start=i, size=25).profile.userId
    client.follow(users)
    time.sleep(5)