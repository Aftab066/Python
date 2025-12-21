#Multilevel Inherritance : Is A way to use a method in derieved class that is asscociated with another 
#derived class And that derieved class is associated with base class

class Animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species
    def showdetailes(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")
        
class Cat(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Cat")
        self.breed = breed
    def showdetailes(self):
        Animal.showdetailes(self)
        print(f"Breed : {self.breed}")
        
class Final(Cat):
    def __init__(self,name,colour):
        Cat.__init__(self,name,breed="Persian")
        self.colour = colour
    def showdetailes(self):
        Cat.showdetailes(self)
        print(f"Colour : {self.colour}")
        
o = Final("Monu","White")
o.showdetailes()
print(Final.mro())