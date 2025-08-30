#Factorial

# def Factorial(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return(num*Factorial(num-1))

# print(Factorial(5))

# Fibonaaci

# def Fibonaaci(f0,f1):
#     if(f0==0 or f1==1):
#         return 1
#     else:
#         return(f0)

def fib(num):
  '''Takes num and returns fibonacci series'''
  if num ==0:
    return 0
  elif num==1:
    return 1
  else:
    return fib(num-1)+fib(num-2)
print(fib.__doc__)
for i in range(5):
  print(fib(i),end=" ")