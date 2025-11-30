# Today We Will Learn Some Methods File IO 
#Readlines
#Writelines

#Readlines 

# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i = i+1
#     lists = f.readline()
#     if not lists :
#         break
#     n1= lists.split(",")[0]
#     c1= lists.split(",")[1]
#     no1= lists.split(",")[2]
#     print(f"My Name is {n1} And I'm From {c1} My Fav No Is {no1}")
#     print(lists)


#Writelines 

f = open('myfile.txt', 'w')
lists = ['Line 1 \n ', 'Line 2 \n ', 'Line 3 \n']
f.writelines(lists)
f.close