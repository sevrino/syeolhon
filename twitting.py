import tweepy
import json
import random

def twitting(message):
    # API Key Load
    with open('./config/setting.json') as json_file:
        json_data = json.load(json_file)

        ver = json_data["ver"]
        apikey = json_data["api_key"]
        apisecret = json_data["apisecret"]
        access_token = json_data["access_token"]
        access_token_secret = json_data["access_token_secret"]
        
    # API Key Load from json files
    auth = tweepy.OAuthHandler(apikey, apisecret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)

# Tweet draw
def draw():
    pass

# Load Tweet Data from json file
def loaddata():
    with open('./config/tweet/tweetting.json') as json_file:
        json_data = json.load(json_file)


def start():
    twitting('트위터 봇 테스트 시작.')
