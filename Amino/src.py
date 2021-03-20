import amino
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
def get_del_msg(info,filename = "messages.json"):
    """this method fetches the last deleted message of the requested chat"""
    chatId = info.chatId
    userId = info.author.userId
    nickname = info.author.nickname
    messageId = info.messageId
    content = info.content

    return None
    # with open(filename) as f:
    #     data = json.load(f)
    #     for chat in data:
    #         if chat.get(chatId) != None:
    #    