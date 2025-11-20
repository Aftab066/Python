import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp>= 6 and timestamp<= 11
):
    print("Good Morning")
elif (timestamp>=12 and timestamp<=16):
         print("Good Afternoon")
elif (timestamp>=17):
         print("Good Evening")
else:
    print("Good Night")


#Thanks
