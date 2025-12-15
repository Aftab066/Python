#dir : used to know all method present in an object
# __dict__ : returns as dictonary attributes
# help : gives a proper documentation of code and description of attributes

# X = [1,2,3]
# print(dir(X))

class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
p = Person("Aftab",1739)
    
print(p.__dict__) #dict method
print(help(Person)) #help method