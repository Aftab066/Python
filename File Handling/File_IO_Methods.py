# Today We Will Learn Some Methods File IO 
#Readlines
#Writelines

#Readlines 

f = open('myfile.txt', 'r')
i = 0
while True:
    i = i+1
    lists = f.readline().strip()
    if not lists :
        break
    
    n1= lists.split(",")[0]
    c1= lists.split(",")[1]
    no1= lists.split(",")[2]
    lists = lists.split(",")
    print(f"My Name is {n1} And I'm From {c1} My Fav No Is {no1}")
    print(type(lists))


#Writelines 

# f = open('myfile.txt', 'w')
# lists = ['Line 1 \n ', 'Line 2 \n ', 'Line 3 \n']
# f.writelines(lists)
# f.close

#Seek() Function Is a function that takes value above seek
#Seek Means To Avoid that index

# f = open('myfile.txt', 'r')
# f.seek(5)
# print(f.read())
# f.close

#Tell() Functions Tells Us That Current Position Of The Function

# f = open('myfile.txt', 'r')
# f.seek(5)
# f.tell()
# print(f.tell())
# print(f.read())
# f.close

#Truncate() Function Prints The Character That Is Truncate for example

# f = open('myfile.txt', 'w')
# f.write("Aftab Is Cool")
# f.truncate(5)
# f.close

# with open('myfile.txt' , 'r') as f:
#     print(f.read())
#Thanks