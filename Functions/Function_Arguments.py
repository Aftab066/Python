# Default Arguments

# def average(a=10,b=10):
#     print("The Average is ",(a+b)/2)

# average()

#So Basically Default Arguments Is That The Default Values Are Given In The Function
#We Can Also Overwrite It

#Required Arguments

# def average(a,b=10):
#     print("The Average is ",(a+b)/2)

# average()

# Required Arguments Means If There Are Two Values To Be Given For The Operation
# Both Values Should Be Present

#Keyword Arguments 

# def average(a=10,b=10):
#     print("The Average is ",(a+b)/2)

# average(b=5,a=5)

#In This Argument We Can Also Change The Order Block AS Shown Above

# Variable Length Arguments

def Numbers(*num):
    sum=0
    for i in num:
     sum = sum + i
    print("The Average Is ",sum/len(num))


Numbers(5,6)

#Sometimes We Have To Add More Arguments Then We Use This
#Thanks