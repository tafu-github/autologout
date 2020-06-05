from pyautogui import *
import schedule


def job():
    button = locateOnScreen('lg_button.png')
    click(x=button.left + button.width/2, y=button.top+button.height/2)
    sys.exit()


schedule.every().day.at("17:35").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

