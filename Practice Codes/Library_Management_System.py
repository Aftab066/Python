
#Library Management With Simple OOPS

class Library:
    books = []
    no_of_books = 0
    def op(self):
        books = input("Enter The Name of book to add it into Library : ")
        print(books)
        #Appends The Book Name Into System
        f = open('myfile.txt', 'a')
        f.write("\t" + books)
        f.close
        #Shows Avalable Books In Library
        f = open("myfile.txt",'r')
        books = f.read().strip()
        print(f"Availeble Books In Library : {books }")
        books=books.split(",") #Converts String Into List
        # print(type(books))
        no_of_books = len(books)
        if(len(books)==no_of_books):
            print("All Okay")
        print(no_of_books)

a = Library()
a.op()

