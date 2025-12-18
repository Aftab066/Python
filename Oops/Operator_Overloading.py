#Operator Overloading : Means Using Operators In class and giving them custo behaiviours 

class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    
    def __add__(self,i):
        return Points(self.x + i.x, self.y + i.y)
    
p1 =Points(1,2)
p2 =Points(3,4)

p3 = p1 + p2
print(p3.x,p3.y)