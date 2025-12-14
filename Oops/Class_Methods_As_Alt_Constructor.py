#Class Method As A Alt Constructor 

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    @classmethod
    def from_str(cls,data):
        return cls(data.split("-")[0],data.split("-")[1])

a = Employee("Aftab",666)
print(a.name)
print(a.id)
data = "Aftab-555"
a1 = Employee.from_str(data)
print(a1.name)
print(a1.id)
