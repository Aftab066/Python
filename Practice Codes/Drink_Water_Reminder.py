import time
import winsound
from plyer import notification

target_time = input("Enter The Time To Remind :-")

while True:
    if time.strftime("%H:%M")== target_time:
        winsound.Beep(1200,800)
        notification.notify(
            title = "Alert",
            message = "Time To Drink Water",
            timeout = 10
        )
        break
    time.sleep(1)