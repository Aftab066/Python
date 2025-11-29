# Basically These Function is used To Avoid Syntax Error Like 
#We Use A Variable In A Conditional Statements It Works Correctly If It Is Defined Earlir 
#If Not It Will Show A error

#Like This 

# A = [1, 2, 3,4,5]

# index = 0
# for a in A:
#     print(a)
#     if(index==2):
#         print("Hey Aftab!")
#     index +=1 

#In This Situation We Declare The Index Varible Outside The Loop
# We Can Do This In A Simple way Using Enumerate Function

A = [1, 2, 3,4,5]

for index , a in enumerate(A):
    print(a)
    if(index==2):
        print("Hey Aftab!")
    index +=1 

#This Also Works As Same As Previous One But Declaration Out Of Box Is Simplified
