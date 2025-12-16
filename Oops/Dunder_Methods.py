#__init__ :Called As Constructor
#__len__ : To Get Len Of Object
#__str__ : 
#__repr__ :
#__call__ : To Make Object Callable

class Employee:
    def __init__(self,name):
        self.name = name
        
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
            
        return i
        
a = Employee("Aftab")
print(a.name)
print(len(a))