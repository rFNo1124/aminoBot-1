import amino
import json
prox = {
    "http": "61.29.96.146:80",
    "https": "51.158.68.68:8761",
}
with open("info_sunil.json", "r") as info:
    data = json.load(info)
    EMAIL = data["email"]
    PASS = data["password"]
    comId = data["community"]

# initializing client 
client = amino.Client(proxies=prox)

res = client.login(email= EMAIL,password= PASS)
if res == 200:
    print("Bot Logged In Successfully.")

sub_client = amino.SubClient(aminoId= comId, profile= client.profile)

# res1 = sub_client.transfer_host(chatId="fb7a5331-af4f-4641-a4f2-564ea585468f", userIds= ["04610bfa-99ab-4101-8285-f3a045becce4"])


# print(res1)
json = sub_client.get_from_code("https://aminoapps.com/u/fexbi16").objectId

self = sub_client.get_user_info(json)
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
        print(f"{i} : {info[i]}")
print(len(info))