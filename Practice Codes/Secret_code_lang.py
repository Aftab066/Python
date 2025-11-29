
msg = input("What Do You want to Do Code Or Decode :  ")
text = ""
letter = ""
codels = []
decodels = []
remove = ""
Remove = ""

#Section 1 : Taking Task From User
if (msg == "Code" or msg == "code"):
    text = input("Enter The Message That You Want To Convert \n It Into Secret Code Lang :")
    
elif (msg == "Decode" or msg == "decode"):
    letter = input("Enter The Message That You Want To Convert \n It Into Simple Language :")
else :
    print("Invalid Input Byee")
    exit()

#Section 2 : Working On Task Given By User For Code The Message 
if(len(text) > 3):
    codels = list(text)
    pick = codels.pop(0)
    codels.append(pick)
    secret1 ='' .join(codels)
    print(secret1)

else:
    codels.reverse()
    secret2 = '' .join(codels)
    print(secret2)
    
#Section 3 : For Decoding The Message

if(len(letter) < 3):
    decodels = list(letter)
    decodels.reverse()
    simple1 = '' .join(decodels)
    print(simple1)
elif(len(letter)>3):
    decodels = list(letter)
    remove = decodels[:3]
    del decodels[:3]
    decodels.extend(remove)
    simple2 = "" .join(decodels)
    print(simple2)

