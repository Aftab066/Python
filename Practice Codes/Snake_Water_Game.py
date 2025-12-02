#Section 1 : To Store Wins And Looses 

results = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
score = []
row = 0
loose = []
draw = []
#Section 2 : Make Choices 

print("Welcome To Snake-Water-Game!!")
usrn = input("Your Pretty Name Please : ") 
print("You Have To Won Atleast 2 Rounds To Win This Game ")

print(f"Hello {usrn} Lets Play The Game :")


import random

#Section 3 : Game Logic

for i in range(3):
    usrc = input("Choose One \n  1. Snake 2. Water  3. Gun 4. Exit () :")
    
    options = ("Snake" , "Water" , "Gun")
    computer_c = random.choice(options)
    if (usrc==computer_c):
        results [row] [2] = 1 
    
    if(usrc == "Snake" and computer_c == "Water") or(usrc == "Water" and computer_c == "Gun") or (usrc == "Gun" and computer_c == "Snake") :
        print("You Win This Round!!")
        results [row] [0] = 1
    row += 1



#Section 3 : Results 


for row1 in range(3):
    if (results [row1] [0] ==1):
        score.append(results[row1][0])
    elif(results [row1] [1] == 1):
        loose.append(results[row1][1])
    elif(results [row1] [2] == 1):
        draw.append(results[row1][2])

    
from functools import reduce

if not score:
    pass
else :
    score = reduce(lambda x, y: x+y, score )

#Loose
if not loose:
    pass
else :
    loose = reduce(lambda x, y: x+y, loose )

#Draw
if not draw:
    pass
else :
    draw = reduce(lambda x, y: x+y, draw )

print(score)

if (score==2):
    print(f"You Won {score} Rounds!!!")
    print("You Are The Winner!!")
elif(loose==2):
    print(f"You Loss {loose} Rounds!!!")
    print("You Lost The Game")
elif(draw==2):
    print(f"{draw} Rounds Are Draw")
    print("It Was A Tie")
else:
    print("Please Play Again")
    exit()