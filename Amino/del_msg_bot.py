import amino
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
if res == 200:
    print("Bot Logged In Successfully.")
sub_client = amino.SubClient(aminoId= comId, profile= client.profile)

def write_json(data,filename = "chats.json"):
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)
def update_json(info,filename = "chats.json"):
    chatId = info.chatId
    userId = info.author.userId
    nickname = info.author.nickname
    messageId = info.messageId
    content = info.content
    with open(filename) as f:
        data = json.load(f)
        temp = data["chats"]
        x = {
            messageId:content
        }
        temp.append(x)
    return data
def get_del_msg(info,filename = "chats.json"):
    chatId = info.chatId
    userId = info.author.userId
    nickname = info.author.nickname
    messageId = info.messageId
    content = info.content
    with open(filename) as f:
        data = json.load(f)
        for message in data["chats"]:
            if message.get(messageId) != None:
                return message[messageId]
@client.event("on_text_message")
def on_text_message(data):
    info = data.message
    print(".")
    info = update_json(info)
    print("..")
    write_json(info)
    print("...")

@client.event("on_delete_message")
def on_delete_message(data):
    info = data.message
    del_msg = get_del_msg(info)
    print(">")
    sub_client.send_message(chatId=info.chatId, message=del_msg)
    print(">>")
