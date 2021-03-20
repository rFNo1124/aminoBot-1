import amino
import json
prox = {
    "http": "61.29.96.146:80",
    "https": "51.158.68.68:8761"
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
print(client.userId)

sub_client = amino.SubClient(aminoId= comId, profile= client.profile)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def user_info_global(cmd : str = None, uId :str = None):
    info = client.get_user_info(uId)
    if cmd == "all":
        key = "g"
        return user_info_all(key = key, uId = uId)
    else:
        return info.cmd

def user_info_local(cmd : str = None, uId : str = None):
    info = sub_client.get_user_info(uId)
    if cmd == "all":
        key = "l"
        return user_info_all(key = key, uId = uId)
    else:
        return info.cmd

def user_info_all(key : str = None, uId : str = None):
    if key == "g":
        self = client.get_user_info(uId)
    else:
        self = sub_client.get_user_info(uId)
    info = {
        "accountMembershipStatus" : self.accountMembershipStatus,
        "activation " : self.activation,
        "activePublicLiveThreadId " : self.activePublicLiveThreadId,
        "aminoId " : self.aminoId,
        "age " : self.age,
        "aminoIdEditable " : self.aminoIdEditable,
        "appleId " : self.appleId,
        "avatarFrame " : self.avatarFrame,
        "avatarFrameId " : self.avatarFrameId,
        "backgroundImage " : self.backgroundImage,
        "backgroundColor " : self.backgroundColor,
        "blogsCount " : self.blogsCount,
        "commentsCount " : self.commentsCount,
        "content " : self.content,
        "coverAnimation " : self.coverAnimation,
        "createdTime " : self.createdTime,
        "customTitles " : self.customTitles,
        "dateOfBirth " : self.dateOfBirth,
        "defaultBubbleId " : self.defaultBubbleId,
        "disabledLevel " : self.disabledLevel,
        "disabledStatus " : self.disabledStatus,
        "disabledTime " : self.disabledTime,
        "email " : self.email,
        "extensions " : self.extensions,
        "facebookId " : self.facebookId,
        "fansCount " : self.fansCount,
        "followersCount " : self.followersCount,
        "followingCount " : self.followingCount,
        "followingStatus " : self.followingStatus,
        "gender " : self.gender,
        "globalStrikeCount " : self.globalStrikeCount,
        "googleId " : self.googleId,
        "icon " : self.icon,
        "influencerCreatedTime " : self.influencerCreatedTime,
        "influencerInfo " : self.influencerInfo,
        "influencerMonthlyFee " : self.influencerMonthlyFee,
        "influencerPinned " : self.influencerPinned,
        "isGlobal " : self.isGlobal,
        "isMemberOfTeamAmino " : self.isMemberOfTeamAmino,
        "isNicknameVerified " : self.isNicknameVerified,
        "itemsCount " : self.itemsCount,
        "lastStrikeTime " : self.lastStrikeTime,
        "lastWarningTime " : self.lastWarningTime,
        "level " : self.level,
        "mediaList " : self.mediaList,
        "membershipStatus " : self.membershipStatus,
        "modifiedTime " : self.modifiedTime,
        "mood " : self.mood,
        "moodSticker " : self.moodSticker,
        "nickname " : self.nickname,
        "notificationSubscriptionStatus " : self.notificationSubscriptionStatus,
        "onlineStatus " : self.onlineStatus,
        "onlineStatus2 " : self.onlineStatus2,
        "phoneNumber " : self.phoneNumber,
        "postsCount " : self.postsCount,
        "privilegeOfChatInviteRequest " : self.privilegeOfChatInviteRequest,
        "privilegeOfCommentOnUserProfile "  : self.privilegeOfCommentOnUserProfile,
        "pushEnabled " : self.pushEnabled,
        "race " : self.race,
        "reputation " : self.reputation,
        "role " : self.role,
        "securityLevel " : self.securityLevel,
        "staffInfo " : self.staffInfo,
        "status " : self.status,
        "storiesCount " : self.storiesCount,
        "strikeCount " : self.strikeCount,
        "tagList " : self.tagList,
        "twitterId " : self.twitterId,
        "userId " : self.userId,
        "verified " : self.verified,
        "visitPrivacy " : self.visitPrivacy,
        "visitorsCount " : self.visitorsCount,
        "warningCount " : self.warningCount,
        "totalQuizHighestScore " : self.totalQuizHighestScore,
        "totalQuizPlayedTimes " : self.totalQuizPlayedTimes,
        "requestId " : self.requestId,
        "message " : self.message,
        "applicant " : self.applicant,
        "avgDailySpendTimeIn7Days " : self.avgDailySpendTimeIn7Days,
        "adminLogCountIn7Days " : self.adminLogCountIn7Days
    }
    for i in info:
        if info[i] != None:
            info.pop(i)
    return info

@client.event("on_text_message")
def on_text_message(data):
    content =  data.message.content
    
    if data.message.title == None:
        print(content)
    if content == "/help":
        msg = f"thanks <$@{str(data.message.author.nickname)}$> for the query but actually i'm still working on updates."
        sub_client.send_message(chatId= data.message.chatId,  message= msg, mentionUserIds=[str(data.message.author.userId)])
    elif str(content).startswith("/findGlobal"):
        print(">")
        sub_client.send_message(chatId=data.message.chatId, message="ok wait")
        print(">")
        key , content = str(content).split("-")  
        print(">")  #e.g -> "/findGlobal-aminoId link"
        command, *links = str(content).split(" ")
        print(">")
        for link in links:
            print(">")  
            userId = client.get_from_code(str(link)).objectId
            info = user_info_global(cmd=command, uId = userId)
            print(">")
            if command == "all":
                msg = str(info)
                print(">")
            else:
                msg = str(info)
                print(">")
            sub_client.send_message(chatId= data.message.chatId, messageType= None, message= msg)
            print(">")
    elif str(content).startswith("/findLocal"):
        sub_client.send_message(chatId=data.message.chatId, message="ok wait")
        key , content = str(content).split("-")  #e.g -> "/findGlobal-aminoId link"
        command, *links = str(content).split(" ")
        for link in links:
            userId = client.get_from_code(str(link)).objectId
            info = user_info_local(cmd=command, uId = userId)
            if command == "all":
                msg = str(info)
            else:
                msg = str(info)
            sub_client.send_message(chatId= data.message.chatId, messageType= None, message= msg)
    
        
@client.event("on_group_member_join")
def on_group_member_join(data):
    
    msg = f"[b]aww thanks for joining . WELCOME <${str(data.message.author.nickname)}$>  !! this is meh <${botSenpai}$> .. ok ok listen , make sure you follow the rules and ofc enjoy your stay !."
    sub_client.send_message(chatId= data.message.chatId, messageType= None, message= msg, mentionUserIds=[str(data.message.author.userId), client.userId]  )
    print("someone joined")

@client.event("on_group_member_leave")
def on_group_member_leave(data):
    msg = f"[b]huh seriously <${str(data.message.author.nickname)}$> you left .. okeh i'm waiting for your comeback ."
    sub_client.send_message(chatId= data.message.chatId, messageType= None, message= msg ,mentionUserIds=[str(data.message.author.userId)] )
    print("someone left")