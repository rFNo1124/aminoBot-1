import json
def write(data,filename = "messages.json"):
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)
def update_json():
    with open("messages.json") as f:
        chatId = "b89188f2-205f-4e3cdc-9df2-cf203ca6b769"
        messageId = "75773368-38eb-4ddc90-9dc5fe-e33994cde539d4"
        content = "baldecco"
        add = {
            chatId:[
                {
                    messageId:content
                }
            ]
        }

        try:
            data = json.load(f)
        except:
            x = []
            write(x)
            data = json.load(f)
        temp = data
        if data != []:
            print("json ain't empty")
            for chat in data:
                print(chat)
                chat_msg_list = chat.get(chatId)
                print(chat_msg_list)
                if chat_msg_list != None:
                    print("chat exits")
                    if len(chat_msg_list) == 10:
                        print("deletine five lines")
                        del chat_msg_list[:5]
                    temp = chat_msg_list
                    print("temp assigned to chat which is a array of dict ")
                    x = {
                        messageId:content
                    }
                    temp.append(x)
                    print("successfully appended msg with content")
                    return data
            temp.append(add)
            print("successfulllty appended a neww chat > inner else")
            return data
        else:
            temp.append(add)
            print("successfullly appended a new chat > outer else ")
            return data
data = update_json()
write(data)