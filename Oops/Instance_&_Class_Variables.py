#Class Variable Is Definied Inside The Class If It Is Changed Outside The Class It Is Changed By The instance variable
# Instance variable is a object associated varible it is definied outside the class 
# The Intrepreter Find required value frist inside Instance var if it does not get it there it goes inside 
#class var if does not get it therealso it shows error

class YC:
    clg = "Yc Karad " # Class Variable
    def __init__(self,name,branch): #The Variables Inside The Constructor Are Instance Variable
        self.name = name
        self.branch = branch
    def id(self):
        print(f"The College name : {self.clg} \n Student name :{self.name} \n Branch : {self.branch}")
    
s1 = YC("Aftab","CS")
s1.clg = "YC Satara" #Update Only For s1 Object The changes are applied before calling the function
s1.id() # After Func executes the default changes are applied
s2 = YC("Omkar","Chemistry") 
s2.id()

