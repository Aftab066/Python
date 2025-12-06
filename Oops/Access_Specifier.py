# In Oops There are 3 access specifiers 
# 1 Private 
# 2 Public Same As Default Variable Anyone Can Access
# 3 Protected Same As Public

# Private

class Employee:
    def __init__(self):
        self.__name = "Aftab"

a = Employee()
# print(a.__name) # Cannot Be Accessed Directly 
print(a._Employee__name) # Cn be accessed Directly using this method