#Short hand If Else Means Whole If Else Statement In One line 
#We Use This Beacuse Programs Becomes More Readble
# Note : It Cannot Be Used In Complex Programs

#Example
x = int(input("Enter The First Integer Of Your Phone No :"))
y = int(input("Enter The Last Integer Of Your Phone No :"))

print(f"{x} is Greater ") if x>y else print(f"{y} is greater ") if x<y else print("Equal")