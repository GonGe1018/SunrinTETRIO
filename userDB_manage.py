import json

userDB=open(file='userDB.json',mode='r').read()

dict = json.loads(userDB)

numOfUser=int(dict["numOfUser"])

def AddUser(name,s_ID,nick,_40L,blitz,rank):
    pass