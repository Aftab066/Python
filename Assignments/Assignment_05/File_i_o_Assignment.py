# Question 1 :
# usr = ["Aftab","Nikhil","Omkar","Ammar","Ismail"]
# with open('name.txt','a+') as f:
#     for i in usr:
#         f.write(f"{i}\n") 

# with open('name.txt','r') as f:
#     # print(f.read)

#Question 2 :

# with open("log.txt", "a+") as f:
#     f.write("Program run Successfully!!! \n")
#     f.seek(0)
#     print(f.read())
    
    
#Question 3 :

# lst = [5,10,15,20,25]

# n_lst = [val  for val in lst if val > 15]

# print(n_lst)

#Question 4 :
# import json
# with open(r"E:\Developer\Git Repo\Python\Assignments\Assignment_05\cities.json","r") as f:
#     data = json.load(f)

# x = input("Enter The City Name : ")
# y = int(input("Enter The Population : "))
# data[x] = y

# with open(r"E:\Developer\Git Repo\Python\Assignments\Assignment_05\cities.json","w") as f:
#     json.dump(data,f,indent=4)

#Question 5 :

# try:
#     with open("data.txt",'r') as f:
#         print(f.read())
        
# except FileNotFoundError:
#     print("File Not Found")
#Thanks