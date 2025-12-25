# Time Module Is Used To Display Time
#time.time Is used for displaying Time In Seconds From 1970 Its The Date When time module was introduced

import time

# print(time.time())

#time.sleep is used for pausing time for any custom time in seconds

# print("Hey see you after 3 seconds")
# time.sleep(3)
# print("I'm Here ")

#time.ctime() for displaying current time in human readable format
# print(time.ctime())

# time.localtime() :- For Local Time format

# t = time.localtime()
# print(t.tm_hour,":",t.tm_min,":",t.tm_sec)

#time.strftime() :- for displaying custom time
# %d :- For Day
# %m :- month
# %Y : - year
# %H :- hour
# %M :- minute
# %S :- second 

t = time.localtime()
Date = time.strftime("%d-%m-%Y",t)
Waqt = time.strftime("%H-%M-%S",t)

print(Date)
print(Waqt)

