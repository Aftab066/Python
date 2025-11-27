#F-String Is A String Formating Like This
# Name = "Aftab"
# Country = "India"
# # print(f"My Name Is {Name}, I am From {Country}")

#Therefore The F Is Use For String Formatting 
#Second Method For String Formatting Is Given Below

text=("My Name Is {}, I am From {}")
print(text.format("Aftab","India"))


subject = (input("Enter The Subject Name : "))
marks = (input("Enter the marks Obtain : "))

print(f"Aftab Got {marks} in {subject}")