from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys

def Window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,500,500)
    win.setWindowTitle("Hello World")
    label = QtWidgets.QLabel(win)
    label.setText("Aftab")
    label.move(100,100)
    
    btn = QPushButton("Click Me",win)
    btn.move(100,200)
    btn.clicked.connect(lambda:print("Alhamdulillah"))
    win.show()
    sys.exit(app.exec())

Window()