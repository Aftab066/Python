# Question 1 :
# usr = ["Aftab","Nikhil","Omkar","Ammar","Ismail"]
# with open('name.txt','a+') as f:
#     for i in usr:
#         f.write(f"{i}\n") 

# with open('name.txt','r') as f:
#     # print(f.read)

#Question 2 :

with open("log.txt", "a+") as f:
    f.write("Program run Successfully!!! \n")
    f.seek(0)
    print(f.read())