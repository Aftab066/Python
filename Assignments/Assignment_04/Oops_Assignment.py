#Question 1 :

# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
        
#     def get_info(self):
#         print(f"The Owner Name :- {self.owner_name}")
#         print(f"The Account Number :- {self.account_number}")
#         print(f"The Availeble Balance :- {self.balance}")
        
#     def deposit(self,Amount):
#         self.Amount = Amount
#         self.balance += Amount
#         print(f"Availeble Balance {self.balance}")
        
#     def withdraw(self,money):
#         self.money = money
#         self.balance-= money
#         print(f"Availeble Balance {self.balance}")
        
#     def show_balance(self):
#         print(f"Availeble Balance {self.balance}")
        
        
# a1 = BankAccount(12345678,"Aftab",10000)

# a1.show_balance()

#Question 2 :

# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author 
#         self.reviews = []
#     def add_reviews(self,review):
#         self.reviews.append(review)
        
#     def count_of_reviews(self):
#         print(f"Total Reviews : {len(self.reviews)}")
        
#     def show_reviews(self):
#         print(f"The Reviews For {self.title} :")
#         for r in self.reviews:
#             print(r)
            
    
# b1 = Book("Power","James")
# b1.add_reviews("Wooh")
# b1.add_reviews("Best")
# b1.add_reviews("Brilliant")
# b1.add_reviews("Awesome")
# b1.count_of_reviews()
# b1.show_reviews()

#Question 3 :

# class Student:
#     def __init__(self,name,marks,roll_no):
#         self.__name = name 
#         self.__marks = marks 
#         self.__roll_no = roll_no 
        
#     def get_info(self):
        
#         return self.__name,self.__roll_no,self.__marks
    
#     def set_info(self,new_n,new_m,new_r):
#         if new_n == None:
#             print("Invalid Value")
#         else:
#             self.__name = new_n
        
#         if new_m< 0 :
#             print("Invalid Value")
#         else:
#             self.__marks = new_m
                
#         if new_r > 1 and new_r < 100 :
#                self.__roll_no = new_r
#         else :
#             print("Invalid Value")
            
# s1 = Student("Aftab",94,21)

# s1.set_info("Nikhil",90,24)
# # s1.set_info(None,-2,101)
# print(s1.get_info())

#Question 5 :

# class Shape:        
#     def Area(self):
#         pass
    
# class Circle :
#     def __init__(self,r):
#         self.r = r
#     def Area(self):
#      return 3.14*self.r*self.r
 
 
# class Square :
#     def __init__(self,a):
#         self.a = a
#     def Area(self):
#      return self.a * self.a
 
# class Rectangle :
#     def __init__(self,l,w):
#         self.l = l
#         self.w = w
#     def Area(self):
#      return self.l*self.w

# c = Circle(5)
# print(c.Area())

# s = Square(5)
# print(s.Area())

# r = Rectangle(6,3)
# print(r.Area())