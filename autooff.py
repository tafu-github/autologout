from pyautogui import *
import schedule
import datetime
import time
import sys
import winsound

def job():
    try:
        button = locateOnScreen('lg_button.png')
        click(x=button.left + button.width/2, y=button.top+button.height/2)
        sys.exit()
        
    #ボタンのクリック動作がうまく行かなかった際に、警告音+メッセージ   
    except:
        for i in range(3):
            winsound.Beep(800,200)
        print('RASの終了にエラーが発生しました!!　手動で立ち下げてください')
        sys.exit()

offhour = input('終了する時刻を入力してください（例　"17:35")')
print(offhour)

#時刻の入力間違い時にシステムのたち下げ
try:
    after = datetime.datetime.strptime(offhour, '%H:%M')
except:
    print('例　"17:35" 入力にエラーがあります。やり直してください。')
    sys.exit()

schedule.every().day.at(offhour).do(job)

while True:
    schedule.run_pending()
    print(1)
    time.sleep(1)

