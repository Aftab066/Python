# Multiplication Table

Num = (input("Enter The Number :"))
print(f"The Multiplication Table Of {Num} is :")

try:
    for i in range(1 , 11):
     print(f"{int(Num)} X {i} = {int(Num)*i}")
except:
    print("Invalid Input")

print("Stop")
#Thanks
