import threading
import time

def func(seconds):
    print(f"{seconds} Seconds Gone")
    time.sleep(seconds)
    
    
time1 = time.perf_counter()    
t1 = threading.Thread(target=func , args=[4])
t2 = threading.Thread(target=func , args=[2])
t3 = threading.Thread(target=func , args=[1])

t1.start()
t2.start()#Starts The Function
t3.start()

t1.join()
t2.join() #Waits Until Function Is Not Fully Executed
t3.join()

time2 = time.perf_counter()  
print(time2-time1)  

#Threading : Is Used To run Multi Programs At Once/Parall
#Thanks
