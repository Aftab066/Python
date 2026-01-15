#Contact Book Application
#Operations: Add Contact, View Contacts, Search Contact, Delete Contact

#Database
contact_Book = {}
usr = ""

#Introduction Section

def introduction():
    print("Welcome to the Contact Book Application!")
    print("You can add, view, search, and delete contacts.")
    print("Let's get started!\n")
    
introduction()

#User Choice Section:

while True:
    print("1_Add")
    print("2_Seach")
    print("3_Update")
    print("4_Delete")
    print("5_Exit")
    usr = (input("Enter The Operation To Be Performed :").lower())
    
    if usr =="add":
        name = input("Enter Name Of The Contact: ")
        if name in contact_Book:
           print("Already Exist")
        else:
            Mob_No = int(input("Enter Mob No :"))
            email = input("Enter Email :")
            Age = int(input("Enter Age :"))
            contact_Book[name] = {"age" :(Age),"Mob" : (Mob_No), "Email": (email) }
            print("Contact Created Successfully!!!")
    elif usr == "search":
        name = input("Enter Name Of The Contact: ")
        if name in contact_Book:
            contact = contact_Book[name]
            print(f'Name : {name},age : {Age}, Mob : {Mob_No},Email :{email}')
        else:
            print("Not Found")
    elif usr == "exit":
        exit()
    print(contact_Book)



#Add Operation:

