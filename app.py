import logger as l
import tweet
import json

with open('./config/setting.json') as json_file:
    json_data = json.load(json_file)
    ver = json_data["ver"]

logger = l.log()
print("프로그램을 실행시켜 주셔서 감사합니다. 프로그램의 버전은 %s입니다. 트위터를 확인해 주세요." % (ver))
start = tweet.twt()