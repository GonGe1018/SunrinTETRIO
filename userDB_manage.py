import json
import GetUserLB

# f=open(file='userDB.json',mode='r')
# userDB=f.read()
# f.close()
# dict = json.loads(userDB)

# numOfUser=int(dict["numOfUser"])


def AddUser(student_info):#student_info(사용자 이름, 닉네임)
    lb=GetUserLB.Get(student_info[1])#리더보드 가져오기
    if(lb=='no user'):
        return('no user')
    
    userDB=open(file='userDB.json',mode='r',encoding="UTF-8").read()#json파일 가져와서 딕셔너리로 변환
    dict = json.loads(userDB)

    numOfUser=int(dict["numOfUser"])#딕셔너리 추가 
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
    newFile = open('userDB.json', 'w',encoding="UTF-8")#저장
    newFile.write(_json)
    newFile.close
    
# student_info = ("유채호","gonge1018")
# AddUser(student_info)