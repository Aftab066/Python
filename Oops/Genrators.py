def my_genrator(a,b):
    for i in a,b:
        i = a + b
        yield i 
        
gen = my_genrator(5,7)
print(next(gen))
gen = my_genrator(8,9) #Adding Values 
print(next(gen)) # If We Will Not Use Next Keyword It Will Show Output In Object Format