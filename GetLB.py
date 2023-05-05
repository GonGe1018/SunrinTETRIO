import requests
import json

def Get(userName):
    LBdict = {
        'name':'',
        'ts':'',
        '40L':'',
        'blitz':'',
        'league':
        {
            'playeds':'',
            'wins':'',
            'rank':''    
        },
        '_id':''
    }
    r = requests.get('https://ch.tetr.io/api/users/'+userName.lower())
    html = r.text
    userInfo_json=json.loads(html)

    r = requests.get('https://ch.tetr.io/api/users/'+userName.lower()+'/records')
    html = r.text
    userRecord_json=json.loads(html)

    #유저 이름
    try:
        LBdict['name']=userInfo_json['data']['user']['username']
    except KeyError:
        return('no user')
    #print('유저 이름 : '+LBdict['name'])

    #유저 가입일
    LBdict['ts']=userInfo_json['data']['user']['ts']
    #print('유저 가입일 : '+ LBdict['ts'])

    #40라인 최고 기록
    try:
        LBdict['40L']=int(userRecord_json['data']['records']['40l']['record']['endcontext']['finalTime'])//1000 #bestRecord
    except TypeError:
        LBdict['40L']='null'
    #print('유저 40L 최고 기록 : %s분 %s초 ' %(LBdict['40L']//60,LBdict['40L']%60))

    #blitz 최고 기록
    try:
        LBdict['blitz']=userRecord_json['data']['records']['blitz']['record']['endcontext']['score']
    except TypeError:
        LBdict['blitz']='null'
    #print('유저 blitz 최고 기록 :',LBdict['blitz'])

    #리그 기록
    LBdict['league']['playeds']=userInfo_json['data']['user']['league']['gamesplayed']
    LBdict['league']['wins']=userInfo_json['data']['user']['league']['gameswon']
    LBdict['league']['rank']=userInfo_json['data']['user']['league']['rank']
    #print('유저 리그 기록\n  플레이한 게임 : %s\n  이긴 게임 : %s\n  랭크 : %s'%(LBdict['league']['played'],LBdict['league']['wins'],LBdict['league']['rank']))

    LBdict['_id']=userInfo_json['data']['user']['_id']
    return(LBdict)