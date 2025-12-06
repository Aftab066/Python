#Inheritance : We Can Use A Class Into A Class And We Can Additionally Add Some Code To It

class Driving:
    def __init__(self,name,candrive):
        self.name = name
        self.candrive = candrive
    def school(self):
        print(f"Name Of Driver {self.name} \n Can Drive {self.candrive}")

a = Driving("Aftab",True)
a.school()

class Dschool(Driving): #Inheritance 
    print("Thanks For Coming!!!")
