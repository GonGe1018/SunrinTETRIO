import json
import GetLB
from datetime import datetime




def AddUser(student_info):#student_info(사용자 이름, 닉네임)
    lb=GetLB.Get(student_info[1])#리더보드 가져오기
    if(lb=='no user'):
        return('no user')
    
    userDB=open(file='./DB/userData.json',mode='r',encoding="UTF-8").read()#json파일 가져와서 딕셔너리로 변환
    dict = json.loads(userDB)

    numOfUser=int(dict["numOfUser"])
   
    for i in range(1,numOfUser+1):#만약 중복이 있으면 
        if(dict[str(i)]['nick']==student_info[1]):
            print(datetime.now(),'사용자명:',student_info[1],' 추가 도중 중복 확인')
            return('overlap user')

    #딕셔너리 추가 
    dict[str(numOfUser+1)]={"name":"","nick":"","_40L":"","blitz":"","rank":""}
    addDict=dict[str(numOfUser+1)]
    addDict["name"]=student_info[0]
    addDict["nick"]=student_info[1]
    addDict["_40L"]=str(lb["40L"])
    addDict["blitz"]=str(lb["blitz"])
    addDict["rank"]=str(lb["league"]["rank"])
    dict["numOfUser"]=str(numOfUser+1)
    numOfUser += 1

    _json = json.dumps(dict, indent = 4, sort_keys = True, ensure_ascii = False)#딕셔너리에서 json으로 변환
    newFile = open('./DB/userData.json', 'w',encoding="UTF-8")#저장
    newFile.write(_json)
    newFile.close

    print(datetime.now(),'사용자명:',student_info[1],'이 DB에 추가 되었습니다')

def updateDB():
    userDB=open(file='./DB/userData.json',mode='r',encoding="UTF-8").read()#json파일 가져와서 딕셔너리로 변환
    dict = json.loads(userDB)

    numOfUser=int(dict['numOfUser'])
    for i in range(1, numOfUser+1):
        #print(dict[str(i)])
        try:
            lb=GetLB.Get(dict[str(i)]['nick'])#리더보드 가져오기
            if(lb=='no user'):
                return('no user')
            dict[str(i)]['_40L']=str(lb['40L'])
            dict[str(i)]['blitz']=str(lb['blitz'])
            dict[str(i)]['rank']=lb['league']['rank']
        except KeyError:
            pass

    _json = json.dumps(dict, indent = 4, sort_keys = True, ensure_ascii = False)#딕셔너리에서 json으로 변환
    newFile = open('./DB/userData.json', 'w',encoding="UTF-8")#저장
    newFile.write(_json)
    newFile.close

    print(datetime.now(),'유저 정보가 업데이트 되었습니다.')

def updateRank():
    userDB=open(file='./DB/userData.json',mode='r',encoding="UTF-8").read()#json파일 가져와서 딕셔너리로 변환
    _dict = json.loads(userDB)
    _40dict={}
    for i in range(1,int(_dict['numOfUser'])+1):
        record=_dict[str(i)]['_40L']

        if(_dict[str(i)]['_40L']=='null'):
            record=9999
        _40dict[str(i)]=int(record)

    _dict=dict(sorted(_40dict.items(), key=lambda x:x[1]))
    #print(_dict)

    _json = json.dumps(_dict, indent = 4, ensure_ascii = False)#딕셔너리에서 json으로 변환
    newFile = open('./DB/rankingData.json', 'w',encoding="UTF-8")#저장
    newFile.write(_json)
    newFile.close
    print(datetime.now(),'랭크가 업데이트 되었습니다.')

    return(list(_dict.items()))


#print(updateRank())
#updateDB()

# student_info = ("유채호","gonge1018")
# AddUser(student_info)