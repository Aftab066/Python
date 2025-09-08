def X1():
     try:
        User=int(input("Enter Number Between 1 And 0 : "))
   
        if(User==1):
            print("You Are Welcome")
        elif(User==0):
            print("Get Lost")
    
     except:
        print("Enter A Valid Input")
     finally:
        print("This Is For Fun ")



X1()