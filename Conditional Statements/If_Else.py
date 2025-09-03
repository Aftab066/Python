# If Else Statement
Age =int(input("Enter Your Age :"))

if(Age>=18):
    print("You Are Eligible To Vote")
else:
    print("You Are Not Eligible To Vote")

# IF-ELE-ELIF Statement
if(Age>=18):
    print("You Are Above 18 You Can Drive")
elif(Age<18):
    print("You Are Above 18 You Cannot Drive")
else:
    print("Thank You!!!!!")

#Nested If
 
Chicken =int(input("Enter The Price Of The Chicken : "))

if(Chicken>=200):
    print("Give Me 1 kg")
elif(Chicken<=200 and Chicken>=150):
    if(Chicken>=180):
        print("Give Me 1.5 Kg")
    elif(Chicken>=160):
        print("Give Me 1.75 Kg")
else:
    print("Give Me 2 Kg")

#Thanks