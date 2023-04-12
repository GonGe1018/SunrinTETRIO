import requests
import json


def GetUserLB(userName):
    r = requests.get('https://ch.tetr.io/api/users/'+userName)
    html = r.text
    userInfo_json=json.loads(html)

    r = requests.get('https://ch.tetr.io/api/users/'+userName+'/records')
    html = r.text
    userRecord_json=json.loads(html)

    #유저 이름
    print('유저 이름 : '+userInfo_json['data']['user']['username'])

    #유저 가입일
    user_ts=userInfo_json['data']['user']['ts']
    print('유저 가입일 : '+ user_ts)

    #40라인 최고 기록
    try:
        user_40L=int(userRecord_json['data']['records']['40l']['record']['endcontext']['finalTime'])//1000 #bestRecord
    except TypeError:
        user_40L='null'
    print('유저 40L 최고 기록 : %s분 %s초 ' %(user_40L//60,user_40L%60))

    #blitz 최고 기록
    try:
        user_blitz=int(userRecord_json['data']['records']['blitz']['record']['endcontext']['score'])
    except TypeError:
        user_blitz='null'
    print('유저 blitz 최고 기록 :',user_blitz)

    #리그 기록
    user_league=[userInfo_json['data']['user']['league']['gamesplayed'],userInfo_json['data']['user']['league']['gameswon'],userInfo_json['data']['user']['league']['rank']]
    print('유저 리그 기록\n  플레이한 게임 : %s\n  이긴 게임 : %s\n  랭크 : %s'%(user_league[0],user_league[1],user_league[2]))


string = input()
GetUserLB(string)


