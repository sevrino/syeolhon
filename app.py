import tweepy
import json
import logging
import logger as log

# API Key Load
with open('./config/setting.json') as json_file:
    json_data = json.load(json_file)

    ver = json_data["ver"]
    apikey = json_data["api_key"]
    apisecret = json_data["apisecret"]
    access_token = json_data["access_token"]
    access_token_secret = json_data["access_token_secret"]

logger = log.logger()


def twitting(message):
    auth = tweepy.OAuthHandler(apikey, apisecret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)


twitting('트위터 봇 테스트 중입니다. 해당 게시물이 올라가면 정상적으로 작동한 것이고, 내 하룻밤이 헛되지 않았음을 의미합니다.')
