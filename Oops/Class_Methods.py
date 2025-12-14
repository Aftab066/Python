#Class Method Works With Class Variable And It Uses Cls As Its Parameter That Refers To Class Not To Object

class Person:
    college = "Yc Karad"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name : {self.name} Age : {self.age} College : {self.college}")
    @classmethod
    def chngclg(cls,clg):
        cls.college = clg
        
a = Person("Aftab",20)
a.show()
Person.chngclg("Yc Satara")
a.show()