#Whenever A child class Is Using Multiple Parent class it is Called as Multiple Inheritance

class Job:
    def __init__(self,name):
        self.name = name

class Domain:
    def __init__(self, role):
        self.role = role
        
class Work(Job,Domain):
    def __init__(self,name,role):
        self.name = name
        self.role = role
    def __str__(self):
        return (f"{self.name} Works As {self.role}")
        
a = Work("Aftab","Gen Ai Engineer")
print(a.name)
print(a.role)
print(a)