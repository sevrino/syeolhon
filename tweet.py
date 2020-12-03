import tweepy
import json
import random
import threading as th

if __name__ == "__main__":
    print("Error")



def twitting(message):
    # API Key Load
    with open('./config/setting.json') as json_file:
        json_data = json.load(json_file)

        apikey = json_data["api_key"]
        apisecret = json_data["apisecret"]
        access_token = json_data["access_token"]
        access_token_secret = json_data["access_token_secret"]
        
    # API Key Load from json files
    auth = tweepy.OAuthHandler(apikey, apisecret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)

def twt():
    # Tweet draw
    number = random.randint(1, 2)

    # Load Tweet Data from json file
    with open('./config/tweet/tweetting.json') as json_file:
        json_data = json.load(json_file)

        tweet = json_data["%d" % (number)]

    # START
    th.Timer(600.0, twt).start()
    twitting(tweet)