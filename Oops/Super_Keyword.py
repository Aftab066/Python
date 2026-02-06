#Super Keyword Is Used To Get Code From Parent Class To Child

class Parentclass:
     def __init__(self,name,id):
         self.name = name 
         self.id = id
    
class Childclass(Parentclass):
    def __init__(self,name,id,clg):
        super().__init__(name,id)
        self.clg = clg
        
    
a = Parentclass("Aftab",555)
a1 = Childclass("Nikhil",111,"Yc Karad")

print(a1.name)
print(a1.id)
print(a1.clg)
print(a.name)
print(a.id)
