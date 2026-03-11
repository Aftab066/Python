'''Args :- Arguments or Positional Arguments
Kwargs :- Keyword Arguments''' 

# def employe(*name): #Args Take Multiple Positinal Arguments denoted by *
#     print(name)
    
# employe("aftab",'omkar','ismail')

def Company(**employe): #Takes Multile Keyword Arguments
    print(employe)
    
Company(name="Aftab",Age=21,ID=666,City="Satara")

def Math(*Num):
    total = 0
    for i in Num:
        total+=i
    return total

print(Math(10,20,30,40,50,60))

