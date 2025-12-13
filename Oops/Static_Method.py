#Static Method :- Its Not Neccessary To Call The  Func With Instance 
#In Class Its Not Necessary To Give Self Argument In a Method Instead Of  It We Can Use Static Method

class Math:
    def __init__(self,num):
        self.num = num
    
    @staticmethod
    def add(a,b):
        return a + b
    
print(Math.add(5,5)) #We Can Call It With The Name Of Class But Cannot Withonly Func Name