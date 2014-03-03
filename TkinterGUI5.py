import tkinter
from tkinter import filedialog
from tkinter import tix
from tkinter import Image

pic = None
filePath = None

class MyGUI:

           def __init__(self): 
                # Create main window 
                self.main_window = tkinter.Tk() 
                # Create label 
                self.label1 = tkinter.Label(self.main_window, text='Hello Welcome to Our GUI')
                # Add the label to the window with the pack function
                self.label1.pack() 
                # Create button
                self.b1 = tkinter.Button(self.main_window, text="Choose a Picture", command=self.openShow)
                # add button
                self.b1.pack()
                # Enter tkinter main loop
                tkinter.mainloop()

           def openShow(self):
                      print ("#2")
                      global filePath
                      global pic
                      filePath = tkinter.filedialog.askopenfilename()


                        
                        #file = pickAFile()
                                   #The pickAFile() function brings up a "file selector dialog", which looks just like what pops up when you use the "Open" dialog in, for example, Microsoft Word.
                        
                        #pic = makePicture(file)
                                   # Now the computer has our picture stored in memory, and we can refer to at any time by referencing "pic". 
                        # If our file were a sound, we could do the same type of thing by using the function makeSound(file) . 
                        # It's important to note that neither of the last two functions (pickAFile() or makePicture(file)) will actually make anything appear. 
                        # So far, things are just stored in the computer's memory, invisible to the user. 
                        
                                 ## ????????
                      print (filePath)
                      photo = tkinter.PhotoImage(file=filePath)
           #openShow()

           def changeText(self):
                # create a message box
                tkinter.messagebox.showinfo("Picture Changer", "Choose a Picture pressed")


#  Global variables ouside of the function, so they can be called by all functions.

#class OpenPic():

           
# Run GUI
mygui = MyGUI()
