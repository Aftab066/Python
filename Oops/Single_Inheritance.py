#Single Inheritance : In this child class can only use one parent class

class Animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species
    def sound(self):
        print("Animal Makes Sound")
        
class Cat:
    def __init__(self,name,species):
        
        Animal.__init__(self,name,species="Cat")
        # self.breed=breed
    def sound(self):
        print("Meow")
        

c = Cat("cat","persian")
c.sound()

a = Animal("Cat","Cat")
a.sound()
        