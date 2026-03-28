#Question 1

s = int(input("Enter The Salary :"))

if (s<30000):
    print(f"The Final Tax Rate : {5/100*s}")
elif(s>30000 and s<70000):
    print(f"The Final Tax Rate : {15/100*s}")
elif(s>70000):
    print(f"The Final Tax Rate : {25/100*s}")
else:
    print("Invalid Amount")
    
    
#Question 2 :
