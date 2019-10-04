# coding: utf-8

#thanks
#原案：twitter:3hiragana_bot様
#ひらがなのランダム生成:https://qiita.com/sora410/items/aad7e17c8c9c35a94f45 qiita:@sora410様
###
import random
import tweepy

CK = "insert key here"  # Consumer API key
CS = "insert secret key here"  # Consumer API secret key
AT = "insert token here"  # Access token
AS = "insert secret token here"  # Access token secret

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

text = ""
for i in range(4):
    text += chr(random.randint(ord('あ'),ord('ん')))
print(text)
api.update_status(text)
