Start = int(input("Enter the start of the range: "))
End = int(input("Enter the end of the range: "))

skip = int(input("Enter The Number To skip :"))

if(Start<=End):
    for i in range(Start , End):
        if(i==skip):
            continue
        print(i)
else:
    print("Start Should Be Less Than End")
        
    
    