import amino
import json
from src import *
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
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def write_json(data,filename = "messages.json"):
    """"this method writes the updated json data into the json file"""
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)
def update_json(info,filename = "messages.json"):
    """this function edits the json file with the new message information and returns the updated json"""
    chatId = info.chatId
    messageId = info.messageId
    content = info.content
    add = {
        chatId:[
            {
                messageId:content
            }
        ]
    }
    with open(filename) as f:
        try:
            data = json.load(f)
        except:
            x = []
            write(x)
            data = json.load(f)
        temp = data
        if data != []:
            for chat in data:
                chat_msg_list = chat.get(chatId)
                if chat_msg_list != None: #''''''''''''''''''''''''''''if the requested chat exists in the json file .
                    if len(chat_msg_list) == 1000:#....................deletes the old 500 messages because of performance issues.
                        del chat_msg_list[:500]
                    temp = chat_msg_list
                    x = {
                        messageId:content
                    }
                    temp.append(x)
                    return data
            temp.append(add)#'''''''''''''''''''''''''''''''''''''''''if it  doesn't find the req chat in that json file then it writes that chat into that json file .
            return data
        else:
            temp.append(add)#.........................................if the json file is empty then it writes a new chat into that json file .
            return data
def write_delete_message(info, filename = "deleted_message.json"):
    """this method writes/updates the last delated mesageID with the specific chat"""
    chatId = info.chatId
    messageId = info.messageId
    with open(filename) as f:
        try:
            data = json.load(f)
        except:
            x = []
            write(x)
            data = json.load(f)
    if data != None:
        for dict in data:
            chat =dict.get(chatId) 
            if chat != None:
                del dict
                x = {
                    chatId:messageId
                }
                data.append(x)
    else:
        x = {
            chatId:messageId
        }
        data.append(x)
    write_json(data,filename="deleted_message.json")
def get_del_msg(info,filename = "messages.json"):
    """this method fetches the last deleted message of the requested chat"""
    chatId = info.chatId
    pass

    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@client.event("on_text_message")
def on_text_message(data):
    print('.')
    info = data.message
    chatId = info.chatId
    messageId = info.messageId
    content = info.content
    info = update_json(info)
    print('..')
    write_json(info)
    print('...')
    if info.content.startswith("//snipe"):
        del_mmsg = get_del_msg(info)
        sub_client.send_message(chatId=info.chatId, message=del_msg)  

@client.event("on_delete_message")
def on_delete_message(data):
    info = data.message
    del_msg = get_del_msg(info)
    print('>')
    # sub_client.send_message(chatId=info.chatId, message=del_msg)
    
    




    
    