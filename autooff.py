from pyautogui import *
import schedule
import datetime

def job():
    button = locateOnScreen('lg_button.png')
    click(x=button.left + button.width/2, y=button.top+button.height/2)
    sys.exit()


offhour = input('終了する時刻を入力してください（例　"17:35")')
print(offhour)
after = datetime.datetime.strptime(offhour, '%H:%M')
schedule.every().day.at(offhour).do(job)

while True:
    schedule.run_pending()
    print(1)
    time.sleep(1)

