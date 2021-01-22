<h1 align="center">
<br>
셜혼
</br>
</h1 align>

<h4 align="center">

**트위터 자동 트윗 프로젝트.**

**트위터에서 셜혼을 만나보세요.**

![Version](https://img.shields.io/badge/python-%E2%89%A53.5-blue?logo=python) ![TwitterBot](https://img.shields.io/badge/Syeolhon-Link-blue?logo=Twitter)
</h4>

---

## 요구 성능
RaspberryPi 2 이상 성능 권장

Python 3.7 이상

## 기능
10분마다 자동으로 사용자가 등록한 문구 중 랜덤한 문구를 트윗합니다.

## 설정

- Python을 설치하고, 필요 패키지를 명령어로 설치합니다.
```
pip install -r requirements.txt
```

- config, log 이름의 폴더를 생성하고, config 안에 tweet이라는 폴더를 생성해 주세요.
- log폴더 안에는 bot.log를 생성해주세요.(빈 파일입니다.)
-  /config 에는 setting.json 파일을 생성하여 주세요. 파일의 양식은 아래 예시 파일 코드가 있습니다.

```
/config/setting.json

{
    "ver": "0.2.0",
    "api_key": "api_key",
    "apisecret": "apisecret",
    "access_token": "access_token",
    "access_token_secret": "access_token_secret"
  }
```

- /config/tweet에서는 tweetting.json을 생성하여 주세요. 파일 양식은 아래 예시 코드가 있습니다.

```
/config/tweet/tweetting.json

{
    "1":"Your Tweet",
    "2":"Your Tweet"
    ...
}
```
