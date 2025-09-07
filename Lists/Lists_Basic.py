#   Lists Is BASICALLY A List Of Item 

Marks = [10,20,30,40,50,60]
print(Marks)

#We Can Access A Specific Index Of List
# Like This

print(Marks[0])

#Negative Indexing

print(Marks[-2])

#TO Jumb On Any Index 

print(Marks[1:4:2])

#If We Have To Access A Specific Value Or A character In Index We Use This

if 20 in Marks:
    print("Availeble")

#In Lists It Caunt Any Statement Or Any Value Or Any String Like This

lst=[i*i for i in range(5) if i%2==0]
print(lst)


#Thanks