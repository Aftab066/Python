#Question 1

"""s = int(input("Enter The Salary :"))

if (s<30000):
    print(f"The Final Tax Rate : {5/100*s}")
elif(s>30000 and s<70000):
    print(f"The Final Tax Rate : {15/100*s}")
elif(s>70000):
    print(f"The Final Tax Rate : {25/100*s}")
else:
    print("Invalid Amount")
    
    """

#Question 2 :

"""def even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)

print(even(1,10))"""

#Question 3:

'''n = (input("Enter The Num :"))

for i in n:
    print(i)'''
    
#Question 4


'''def count(n):
    x=0
    for i in n:
        x+=1
        
    return x

n = input("Enter The Num : ")
print(count(n))'''


#Question 5 :

'''def sum (n):
    x=0
    for i in range(1,n+1):
        x+=i
    return x

n = int(input("Enter The Number : "))
print(sum(n))
'''
#Question 6:

'''for i in range(1,101):
    if (i%3==0 and i%5==0):
        print(i)'''
        
        
#Question 7 :

'''while True:
    x = input("Enter The Number : ")
    if(x.lower()=="quit" or x.lower()=='exit'):
        print("Program Ended")
        break
    
    n = float(x)
    if((n>0)):
        print(f"The Number Is Positive : {n}")
    elif((n<0)):
        print(f"The Number Is Negative : {n}")
    else:
        print(f"The Number Is Neutral {n}")'''
        
        
# Question 8 :

'''def calculator(a,b,operator):
    if(operator=='+'):
        print(f"The Addition Of {a} + {b} : ",a+b)
    elif(operator=='-'):
        print(f"The Subtraction Of {a} - {b} : ",a-b)
    elif(operator=='*'):
        print(f"The Multiplication Of {a} X {b} : ",a*b)
    elif(operator=='/'):
        print(f"The Division Of {a} / {b} : ",a/b)
    else:
        print("Enter The Valid Operator!")
        
a = int(input("Enter The Num 1 Twinn!"))
b = int(input("Enter The Num 2 Twinn!"))
operator = input("Enter The Operator  Twinn! (+,-,*,/)")

calculator(a,b,operator)'''

#Question 9 :

'''def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
        else:
            return True
        
n = int(input("Enter The Num : "))
print(is_prime(n))'''

#Question 10 :


while True:
    n = ("Enter the Number To Guess")
    x=210
    if(n>x):
      print("Too High ")
    elif(n<x):
      print("Too Low")
    elif(n==x):
      print("Correct")
            
    


