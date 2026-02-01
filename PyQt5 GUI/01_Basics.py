from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def Window():
    app = QApplication(sys.argv) #Soul Of PyQt5 If It Is not there it will not run code
    win = QMainWindow() # Main Window
    win.setGeometry(200,200,500,500) #Size Of Our Window 
    win.setWindowTitle("Hello World!!!") #Title Of Our Application
    label = QtWidgets.QLabel(win) #Text Inside Window
    label.setText("Aftab") #Label Data
    label.move(100,100) #Moves The Label 
    win.show() #Pop Ups Window
    sys.exit(app.exec()) # Keeps Window Stay Open until We Exit 

Window()