# step1.관련 패키지 및 모듈 import
import schedule
import manageDB
import time

manageDB.updateDB()
manageDB.updateRank()

def _updateDB():
    manageDB.updateDB()
    manageDB.updateRank()
    print('DB가 자동 업데이트 되었습니다')


    

# step3.실행 주기 설정
schedule.every(5).minutes.do(_updateDB)

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)