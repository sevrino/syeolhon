import tweepy
import json
import random
import threading as th

if __name__ == "__main__":
    print("Error")

def twitting(message):
    # API Key Load
    with open('./config/setting.json', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)

        apikey = json_data["api_key"]
        apisecret = json_data["apisecret"]
        access_token = json_data["access_token"]
        access_token_secret = json_data["access_token_secret"]
        
    # UPLOAD Function
    auth = tweepy.OAuthHandler(apikey, apisecret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)


def twt():
    # Tweet draw
    number = random.randint(1, 9)

    # Load Tweet Data from json file
    with open('./config/tweet/tweetting.json', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
        tweet = json_data["%d" % (number)]

    # START
    th.Timer(600.0, twt).start()
    twitting(tweet)

"""
def twt():
    # Tweet draw
    number = random.randint(1, 9)

    # Load Tweet Data from json file
    with open('./config/tweet/tweetting.json', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)

        tweet = json_data["%d" % (number)]

    with open('./config/setting.json', encoding='UTF-8') as timer:
        timer_json = json.load(timer)
        timer_v = timer_json["Timer"]
        timer = timer_json["%d" % (timer_v)]
"""
