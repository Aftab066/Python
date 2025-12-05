#Decorator is a Function Which Adds A Greeting Or Any Thing In Starting And Ending Of Program

def aftab(a):
    def omkar():
        print("Hey Aftab")
        a()
        print("Bye Lots Of Thanks")
    return omkar

@aftab
def hello():
    print("This is Decorator")

hello()