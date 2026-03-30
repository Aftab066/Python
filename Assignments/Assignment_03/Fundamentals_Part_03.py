# #Question 1

# '''usr = input("Enter The Word : ")

# r = usr[::-1]

# if (usr==r):
#     print("Its A Palindrome")
# else:
#     print("Not A Palindrome")'''
    
# #Question 2 :

# '''usr = (input("Enter The Numbers : ")).split()
# x = 0
# for i in usr:
#     x+=int(i)
#     final =  x/len(usr)
    
# print(final)'''

# #Question 3 : 

# '''usr1 = (input("Enter The Numbers : ")).split()
# usr2 = (input("Enter The Numbers : ")).split()

# final = usr1+usr2
# final.sort()

# print(final)'''

# # Question 4 :

# '''tup = (1,2,3,4,5,6,7,8,9)
# tup2 = tuple(x for x in tup if x %2==0)
# tup3 = tuple(y for y in tup if y %2==1)

# print(tup2)
# print(tup3)
# '''
# #Question 5 :
# '''info = {}
# while True:
    
#     print("Welcome To Student Managemnet System ")
#     print("\nA: Add Student \n B: Update Marks \n C:Search For Student \n D: Display All Student And Marks\n E: Exit ()")

#     usr = input("Enter The Input To Proceed : ").lower()
    
#     if (usr=='a'):
#        n = input("Enter The Name Of Student :")
#        if(n in info):
#            print("Already Exist")
#        else:
#             m = int(input("Enter The Marks : "))
#             info[n]=m
#             print(f"Added Succesfully{info}")
#     elif(usr=='b'):
#         n = input("Enter The Name Of Student :")
#         if(n in info):
#             m = int(input("Enter The Marks : "))
#             info[n]=m
#             print(f"Updated Marks {info}")
#         else:
#             print("Student Does Not Exists")
#     elif(usr=='c'):
#         n = input("Enter The Name Of Student :")
#         if(n in info):
#             print(f'{n} {info[n]}')
#         else:
#             print("Student Does Not Exists")
#     elif(usr=='d'):
#         if(info=={}):
#             print("No Data Availeble")
#         else:
#             for keys,values in info.items():
#                 print(f"{keys} : {values}")
#     elif(usr=='e'):
#         print("Exited Succesfully")
#         break
#     else:
#         print("Enter The VALID input")
#             '''
            
# #Question 6 :

# '''Fruits = ["Apple","Banana","Kiwi","Cherry","Mango"]
# f = {}

# for i in Fruits:
#     f[i] = len(i)
    
    
# print(f)'''

# #Question 7 & 9:

# x = input("Enter The Numbers : ").split()
# y = input("Enter The Numbers : ").split()

# s1 = set()
# s2 = set()
# d1 = set()
# d2 = set()

# for i in x:
#     if (i in s1):
#         d1.add(i)
#     else:
#         s1.add(i)
        
# for j in y:
#     if (j in s2):
#         d2.add(j)
#     else:
#         s2.add(j)
        
# print(s1)
# print(s2)

#Question 8:

# usr = input("Enter The Input")
# count=0
# for i in usr:
#     if(i==" "):
#         count+=1
    
    
    
# print(count)

#Question 10 :

# x = input("Enter The String : ")

# s1 = set(x)
# count=len(s1)


# print(s1,count)