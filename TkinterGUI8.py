import tkinter
from tkinter import filedialog
from tkinter import tix
from tkinter import Image

#  Global variables ouside of the function, so they can be called by all functions.

pic = None
filePath = None

class MyGUI:

           def __init1__(self): 
                # Create second window 
                self.second_window = tkinter.Tk() 

           def __init__(self): 
                # Create main window 
                self.main_window = tkinter.Tk() 
                # Create label 
                self.label1 = tkinter.Label(self.main_window, text='Hello Welcome to Our GUI')
                # Add the label to the window with the pack function
                self.label1.pack() 

                # Create button
                self.b1 = tkinter.Button(self.main_window, text="Choose a Picture", command=self.create_button_with_scoped_image)
                # add button
                self.b1.pack()

                # Create button
                self.b2 = tkinter.Button(self.main_window, text="Make Picture Black and White", command=self.create_button_with_scoped_image)
                # add button
                self.b2.pack()
                
                # Enter tkinter main loop
                tkinter.mainloop()
           
           

           def create_button_with_scoped_image(self):
                   print ("#1")   # Debug statement
                   filePath = tkinter.filedialog.askopenfilename()

                   print (filePath)   # Debug Statement
                   img = tkinter.PhotoImage(file=filePath)

                   button = tkinter.Button(self.second_window, image=img)
                   button.img = img  # store a reference to the image as an attribute of the widget
                   button.grid()

           
# Run GUI
mygui = MyGUI()


#openShow()

           #def changeText(self):
                # create a message box
           #  tkinter.messagebox.showinfo("Picture Changer", "Choose a Picture pressed")

