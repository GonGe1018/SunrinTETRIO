import json

def updateRank():
    userDB=open(file='./DB/userDB.json',mode='r',encoding="UTF-8").read()#json파일 가져와서 딕셔너리로 변환
    _dict = json.loads(userDB)
    _40dict={}
    for i in range(1,int(_dict['numOfUser'])+1):
        record=_dict[str(i)]['_40L']

        if(_dict[str(i)]['_40L']=='null'):
            record=1234
        _40dict[str(i)]=int(record)

    _dict=dict(sorted(_40dict.items(), key=lambda x:x[1]))
    print(_dict)

    _json = json.dumps(_dict, indent = 4, ensure_ascii = False)#딕셔너리에서 json으로 변환
    newFile = open('./DB/rankingDB.json', 'w',encoding="UTF-8")#저장
    newFile.write(_json)
    newFile.close


