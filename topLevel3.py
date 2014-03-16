import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import tix
from tkinter import Image


#  Global variables ouside of the function, so they can be called by all functions.

pic = None
filePath = None
img = None

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Open Pic', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        fileDirectory = tkinter.filedialog.askopenfilename()
        print(fileDirectory)

        #self.im.show()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow, fileDirectory)

class Demo2:
    def __init__(self, master, fileDirectory):
        global img
        print ("1")
        self.master = master
        self.frame = tk.Frame(self.master)
        print ("2")
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)

        self.BnWButton = tk.Button(self.frame, text = 'Make Black and White', width = 25, command = self.BnW_windows)
        img = tk.PhotoImage(file = fileDirectory)

    
        button = tk.Button(self.master, image=img)
        button.img = img;
        print ("3")
        button.pack()    #  This packs the image on the button
        print("4")

        self.quitButton.pack()
        self.BnWButton.pack()

        self.frame.pack()
        
        
    def close_windows(self):
        self.master.destroy()

    def BnW_windows(self):
        print ("5")
        global img
        blackPixel = (0, 0, 0)
        whitePixel = (255, 255, 255)
        for y in range(img.height()):
            for x in range(img.width()):
                print ("6")
                pixel= img.get(x, y)
                # print (type(pixel))  Print the type of the pixel which is a str class.
                average = (pixel.getred() + pixel.getgreen() + pixel.getblue())
                if average < 128:
                    pixel.setRed(0)
                    pixel.setGreen(0)
                    pixel.setBlue(0)
                else:
                   pixel.setRed(255)
                   pixel.setGreen(255)
                   pixel.setBlue(255)
        repaint(img)

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
