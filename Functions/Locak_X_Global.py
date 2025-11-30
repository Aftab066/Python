
#Local Variable Is A Variable Which Is Created Inside A Function We Can Use It Only Inside The Function
#Global Variable Is A Variable IWhich Is Created Outside The Function Block It Can Be Used All Over The Function 

#For Example 

a = 6 # Global Variable

def Aftab():
    b = 7 # Local Variable
    a = 9
    print(a)
    print(b)

Aftab()
print(a)
# print(b) #Shows Error Because Its Local Variable Can Be Called Only Inside Function

#Here We Clearly See That We Can't Overwrite The Global Variable In Function Like This
#But We Can Overwrite The Global Variable Only If We Use Global Keyword Inside Function

x = 1 # Global Variable

def Aftab():
    global x 
    y = 2 # Local Variable
    x = 3
    print(x)
    print(y)

Aftab()
print(x)

#Here We Overwrited The Variable Using Global Keyword