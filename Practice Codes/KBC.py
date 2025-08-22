Questions = ["Who was the first President of India","In what year did India gain independence",
"What is the capital of India","Who is known as the Father of the Nation in India",
"Which planet is known as the 'Red Planet'","Who invented the telephone","What is the national animal of India",
"What is the largest ocean on Earth","Who developed the theory of relativity","What is the name of the first artificial satellite launched into space"]

CAns=["Dr Rajendra Prasad",1947,"New Delhi","Mahatma Gandhi","Mars","Alexander Graham Bell",
"The Bengal tiger","The Pacific Ocean","The Pacific Ocean","Sputnik 1"]

Prize=[]


print("Welcome To KBC Kaun Banega Crorepati")
Name=input("Enter Your Name\n")
Ans1=input("Are You Ready To Play KBC\n")

if(Ans1=="Yes" or Ans1=="yes"):
    print("Here We Go",Name, "Lets Play Kaun Banega CrorePati\n")
else:
    print("Thankyou!!!")

print("Here's Our First Question Mr.",Name,"On Your Computer Screen\n")

#Question 1
print(Questions[0])
Ans2=input("Your Answer /Type Exit To Quit \n")

if(Ans2==CAns[0]):
    print("Congrats",Name,"You Won 20 Thousand Rupees")
    Prize.append(20000)
elif(Ans2=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Successfully")
    exit()
else:
    print("Invalid")


Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Second Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()

#Question 2
print(Questions[1])
Ans3=int(input("Your Answer\n"))

if(Ans3==CAns[1]):
    print("Congrats",Name,"You Won 40 Thousand Rupees")
    Prize.append(40000)
elif(Ans3=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Sucessfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Third Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()



#Question 3
print(Questions[2])
Ans4=input("Your Answer\n")

if(Ans4==CAns[2]):
    print("Congrats",Name,"You Won 80 Thousand Rupees")
    Prize.append(80000)
elif(Ans4=="Exit"):
    print("Sorry",Name,"You Lost The Game")
     print("Exited Sucessfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Fourth Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()


#Question 4
print(Questions[3])
Ans5=input("Your Answer\n")

if(Ans5==CAns[3]):
    print("Congrats",Name,"You Won 1 Lack 60 Thousand Rupees\n")
    Prize.append(160000)
elif(Ans5=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Sucessfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Fifth Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()


#Question 5
print(Questions[4])
Ans5=input("Your Answer\n")

if(Ans5==CAns[4]):
    print("Congrats",Name,"You Won 3 Lack 20 Thousand Rupees\n")
    Prize.append(320000)
elif(Ans5=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Sucessfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Sixth Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()


#Question 6
print(Questions[5])
Ans5=input("Your Answer\n")

if(Ans5==CAns[5]):
    print("Congrats",Name,"You Won 6 Lack 40 Thousand Rupees\n")
    Prize.append(640000)
elif(Ans5=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Sucessfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Seventh Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()


#Question 7
print(Questions[6])
Ans5=input("Your Answer\n")

if(Ans5==CAns[6]):
    print("Congrats",Name,"You Won 12 Lack 80 Thousand Rupees\n")
    Prize.append(1280000)
elif(Ans5=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Sucessfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Eighth Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()


#Question 8
print(Questions[7])
Ans5=input("Your Answer\n")

if(Ans5==CAns[7]):
    print("Congrats",Name,"You Won 25 Lack 60 Thousand Rupees\n")
    Prize.append(2560000)
elif(Ans5=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Successfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Ninth Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()


#Question 9
print(Questions[8])
Ans5=input("Your Answer\n")

if(Ans5==CAns[8]):
    print("Congrats",Name,"You Won 51 Lack 20 Thousand Rupees\n")
    Prize.append(5120000)
elif(Ans5=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Successfully")
    exit()
else:
    print("Invalid")

Proceed=input("Want To Play Next Yes/No\n")
if(Proceed=="Yes" or Proceed=="yes"):
    print("Here's Our Tenth Question Mr.",Name,"On Your Computer Screen\n")
else:
    print("Exited You Won ",Prize,"Money ")
    exit()


#Question 10
print(Questions[9])
Ans5=input("Your Answer\n")

if(Ans5==CAns[9]):
    print("Congrats",Name,"You Won 1 Crore Rupees\n")
    print("At The End Mr.",Name,"Won KBC And 1 Cr Prize\n")
    Prize.append(1000000)
elif(Ans5=="Exit"):
    print("Sorry",Name,"You Lost The Game")
    print("Exited Succesfully")
    exit()
else:
    print("Invalid")




