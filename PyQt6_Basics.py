from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
    #We need one and only one instance per Applicaiton
    #We need to pass the sys.argv to allow command line arguments
    #If you know you won't use command line arguments, QApplication([]) is acceptable

#We need to create a widget which will be our window
Window = QWidget()
Window.show() # This is very Important !!! as Windows are hidden by default

#start the event loop
app.exec()

# Your application will not reach here until you exit and the event loop has stopped