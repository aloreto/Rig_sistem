import sys
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QDialog,  QLineEdit
from PySide2.QtCore import Slot


# Greetings

class myTool():
    
    def __init__(self):
    
        # Create a button
        self.button = QPushButton("Click me")
        
        # Connect the button to the function
        self.button.clicked.connect(say_hello)
        
        # Show the button
        self.button.show()


    def say_hello(self):
        print("Button clicked, Hello!")
    
        


# show the window 
myTool = myTool() 
myTool.show()