#In File Handling We Can Read ,Write,Append In a Text File 
#Simple Synatx For File Handling

# f = open('Myfile.txt', 'r')
# print(f) #It Will Show Error If File Is Not Created

#In The Syntax the r is for the read mode 
# there are three modes
# r = read (If The File Is Not Created It will show error and in this mode you can only read the file)
# w = write (In this mode we write a txt in a txt file and if the file already contain some text it will overwrite it )
# a = append (It Will add the text at the end of the content)

#Read 
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close

# #Write
# f = open('myfile.txt', 'w')
# f.write("Hello Aftab ")
# f.close

#Append
# f = open('myfile.txt', 'a')
# f.write("Hello Aftab ")
# f.close

# f = open('Myfile.txt', 'r t') # Here t Is For Text file t is by default and is for b like below
# f = open('Myfile.txt', 'r b') # b for bin or other files