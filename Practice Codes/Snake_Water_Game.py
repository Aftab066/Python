#Section 1 : To Store Wins And Looses 

results = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]


#Section 2 : Make Choices 

print("Welcome To Snake-Water-Game!!")
usrn = input("Your Pretty Name Please : ") 

print(f"Hello {usrn} Lets Play The Game :")


import random

#Section 3 : Game Logic
row = 0
for i in range(3):
    usrc = input("Choose One \n  1. Snake\n 2. Water \n 3. Gun\n 4. Exit () \n:")
    
    options = ("Snake" , "Water" , "Gun")
    computer_c = random.choice(options)
    if (usrc==computer_c):
        results [row] [2] = 1 
    
    if(usrc == "Snake" and computer_c == "Water") or(usrc == "Water" and computer_c == "Gun") or (usrc == "Gun" and computer_c == "Snake") :
        print("You Win This Round!!")
        results [row] [0] = 1
    row += 1

print(results)
