# Constructor is used to Intialize value to object 
# Constructor is Automatically Called For Example

#Default Constructor
# class Driving:
#     def __init__(self):
#         print("Hey Aftab Nice To Meet You!!")

# n = Driving()

#Parametized Constructor 
class Driving:
    def __init__(self,n,cd):
        print("Hey Aftab Nice To Meet You!!")
        self.n = n
        self.cd = cd

    def Drive(self):
        print(f"Name : {self.n} \n Can Drive : {self.cd}")

n = Driving("Aftab","Yes")
n.Drive()

#Parametrized Constructor : We Don't Need To Give A Default Values