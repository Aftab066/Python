from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys

def Window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,500,500)
    win.setWindowTitle("Hello World")
    label = QtWidgets.QLabel(win)
    def Text():
        label.setText("Alhamdulillah")
    label.move(100,100)
    
    btn = QPushButton("Click Me",win) #Creates A Button In Window
    btn.move(100,200) #Position Of Button
    btn.clicked.connect(Text) #Data To Be Executed When Clicked
    win.show()
    sys.exit(app.exec())

Window()