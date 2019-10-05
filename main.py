#!/usr/bin/python
# coding: utf-8

# thanks
# 原案：twitter:3hiragana_bot様
# ひらがなのランダム生成:https://qiita.com/sora410/items/aad7e17c8c9c35a94f45 qiita:@sora410様
# Pythonistaなら知ってるオプションパーサ:https://qiita.com/petitviolet/items/aad73a24f41315f78ee4#sysargv%E3%82%92%E4%BD%BF%E3%81%86 qiita:@petitviolet様
###
from __future__ import unicode_literals
import random
import sys

CK = "insert key here"  # Consumer API key
CS = "insert secret key here"  # Consumer API secret key
AT = "insert token here"  # Access token
AS = "insert secret token here"  # Access token secret
tweeting = True
length = 4
text = ""
usage = 'Usage: python3 {} FILE [-n|--no-tweet] [-l|--length <number>] [-h|--help]'.format(__file__)

if 1 < len(sys.argv):
    arguments = sys.argv
    arguments.pop(0)
    fname = arguments[0]
    options = [option for option in arguments if option.startswith('-')]
    if '-h' in options or '--help' in options:
        print(usage)
        exit()
    if '-n' in options or '--no-tweet' in options:
        tweeting = False
    if '-l' in options or '--length' in options:
        length_position = arguments.index('-l') \
            if '-l' in options else arguments.index('--length')
        length = int(arguments[length_position + 1])

for i in range(length):
    if sys.version_info[0] < 3:
        text += unichr(random.randint(ord('あ'), ord('ん')))
    else:
        text += chr(random.randint(ord('あ'), ord('ん')))
print(text)

if tweeting == True:
    import tweepy

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    api.update_status(text)
