import Tkinter
import Tkinter as tk
import tkFileDialog
from Tkinter import Image
from PIL import Image
from PIL import ImageOps



#  Global variables ouside of the function, so they can be called by all functions.

pic = None
filePath = None
img = None
PILimg= None
edit=None

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Open Pic', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        fileDirectory = tkFileDialog.askopenfilename()
        print(fileDirectory)

        #self.im.show()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow, fileDirectory)

class Demo2:
    def __init__(self, master, fileDirectory):
        global img
        global PILimg
        global edit
        
        #  print ("1")
        self.master = master
        self.frame = tk.Frame(self.master)
        #  print ("2")
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)

        self.BnWButton = tk.Button(self.frame, text = 'Make Black and White', width = 25, command = self.BnW_windows)
        img = tk.PhotoImage(file = fileDirectory)
        PILimg=Image.open(fileDirectory)
        edit=PILimg.load()

        self.MCButton = tk.Button(self.frame, text = 'Make Monochrome', width = 25, command = self.MC_windows)
        img = tk.PhotoImage(file = fileDirectory)
        PILimg=Image.open(fileDirectory)
        edit=PILimg.load()

        self.MirrorImageButton = tk.Button(self.frame, text = 'Mirror Image', width = 25, command = self.MirrorImage_windows)
        img = tk.PhotoImage(file = fileDirectory)
        PILimg=Image.open(fileDirectory)
        edit=PILimg.load()

        self.TransposeButton = tk.Button(self.frame, text = 'Transpoe Top to Bottom', width = 25, command = self.Transpose_windows)
        img = tk.PhotoImage(file = fileDirectory)
        PILimg=Image.open(fileDirectory)
        edit=PILimg.load()
        
        button = tk.Button(self.master, image=img)
        button.img = img;
        #  print ("3")
        button.pack()    #  This packs the image on the button
        #  print("4")

        self.quitButton.pack()
        self.BnWButton.pack()
        self.MCButton.pack()
        self.MirrorImageButton.pack()
        self.TransposeButton.pack()
        
        self.frame.pack()
        
        
    def close_windows(self):
        self.master.destroy()

##  This definition makes our picture Black and White.
##  Referenced:  http://stackoverflow.com/questions/9506841/using-python-pil-to-turn-a-rgb-image-into-a-pure-black-and-white-image
    def BnW_windows(self):
        #  print ("5")
        global img
        global PILimg
        global edit
                    
        print (PILimg)
        PILimg=PILimg.convert('1') # convert image to black and white
        PILimg.show()
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/testBnW.gif", format=None)

##  This definition makes our picture Monochrome.
##  Referenced:  http://stackoverflow.com/questions/9506841/using-python-pil-to-turn-a-rgb-image-into-a-pure-black-and-white-image
    def MC_windows(self):
        #  print ("7")
        global img
        global PILimg
        global edit

        print (PILimg)
        PILimg=PILimg.convert('L') # convert image to monochrome - this works
        PILimg.show()
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/testMONOCHROME.gif", format=None)

##  This definition makes our picture a Mirror Image.
## effbot.org/imagingbook/imageops.htm
    def MirrorImage_windows(self):
        #  print ("8")
        global img
        global PILimg
        global edit

        print (PILimg)
        PILimg=ImageOps.mirror(PILimg)# convert image to a Mirror Image
        PILimg.show()
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/testMIRROR.gif", format=None)

    def Transpose_windows(self):
        #  print ("9")
        global img
        global PILimg
        global edit

        print (PILimg)
        PILimg=PILimg.rotate(180) # Transpose image to Top to Bottom
        PILimg.show()
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/testTRANSPOSE.gif", format=None)


def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()

