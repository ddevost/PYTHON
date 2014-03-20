import Tkinter
import Tkinter as tk
import tkFileDialog
##  from Tkinter import tix
from Tkinter import Image
from PIL import Image
import PIL.ImageOps
import webbrowser

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

        self.NegativeButton = tk.Button(self.frame, text = 'Make Negative', width = 25, command = self.Negative_windows)
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
        self.NegativeButton.pack()
        self.TransposeButton.pack()
        
        self.frame.pack()
        
        
    def close_windows(self):
        self.master.destroy()

    ##  This definition makes our picture Balck and White.
    ##  Referenced:  http://stackoverflow.com/questions/9506841/using-python-pil-to-turn-a-rgb-image-into-a-pure-black-and-white-image
    def BnW_windows(self):
        #  print ("5")
        global img
        global PILimg
        global edit
        
##        blackPixel = (0, 0, 0)
##        whitePixel = (255, 255, 255)
##        for y in range(img.height()):
##            for x in range(img.width()):
####                print ("6")
####                print (img)     # Prints pyimage1
##                pixel= img.get(x, y)   
####                print (pixel)   # Prints 255 255 255
####                print (type(pixel))  # Prints <class 'str'>
####                print (type(PILimg))
##                variable=pixel.split(" ")   # Takes the number in pixel and splits it three ways
##                average = ( (int(variable[0]) + int(variable[1]) + int(variable[2])) /3)
##                if (average < 127):
##                    edit[x, y]=(255)
##                else:
##                    edit[x, y]=(0)
                    
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
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/testMonochrome.gif", format=None)

    ##  This definition makes our picture Negative.
    def Negative_windows(self):
        #  print ("8")
        global img
        global PILimg
        global edit

        print (PILimg)
        PILimg=PILimg.convert("In") # convert image to Negative
        PILimg.show()
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/testNegative.gif", format=None)

    def Transpose_windows(self):
        #  print ("8")
        global img
        global PILimg
        global edit

        print (PILimg)
        PILimg=PILimg.im.transpose(90) # Transpose image to Top to Bottom
        PILimg.show()
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/Transpose.gif", format=None)


def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()

