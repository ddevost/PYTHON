import Tkinter
import Tkinter as tk
import tkFileDialog
##  from Tkinter import tix
from Tkinter import Image
from PIL import Image
from PIL import ImageOps
from pygame import mixer
import scipy.io.wavfile
import matplotlib.pyplot as plt

#  Global variables ouside of the function, so they can be called by all functions.

pic = None
filePath = None
img = None
PILimg= None
edit=None
global paused

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Open Pic', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

        self.button2 = tk.Button(self.frame, text = 'Open a Sound', width = 25, command = self.new_window2)
        self.button2.pack()
        self.frame.pack()

    def new_window(self):
        fileDirectory = tkFileDialog.askopenfilename()
        print(fileDirectory)

        #self.im.show()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow, fileDirectory)

    def new_window2(self):
        fileDirectory = tkFileDialog.askopenfilename()
        print(fileDirectory)


        #self.im.show()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo3(self.newWindow, fileDirectory)

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

    ##  This definition makes our picture Balck and White.
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
        #  print ("8")
        global img
        global PILimg
        global edit

        print (PILimg)
        PILimg=PILimg.rotate(180) # Transpose image to Top to Bottom
        PILimg.show()
        PILimg.save("/Users/DANADEVOST/Desktop/PYTHON_FOLDER/GIF_IMAGES/Transpose.gif", format=None)


class Demo3:
    def __init__(self, master, fileDirectory):
        global paused
        print ("1")
        self.fileDirectory = fileDirectory
        mixer.init(44100)
        self.master = master
        self.frame = tk.Frame(self.master)
        print ("2")
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)

        self.d1 = mixer.Sound(fileDirectory)
        ##d1.play()

        playButton = tk.Button(self.frame, text = 'Play', width = 10, command = self.playSound)
        stopButton = tk.Button(self.frame, text = 'Stop', width = 10, command = self.stopSound)
        pauseButton = tk.Button(self.frame, text = 'Pause', width = 10, command = self.pauseSound)
        wavFormButton = tk.Button(self.frame, text = 'Wav Form', width = 10, command = self.waveForm)
        

        
        #img = tk.PhotoImage(file = fileDirectory)
        #button = tk.Button(self.master, image=img)
        #button.img = img;
        print ("3")
        #button.pack()
        print("4")


        print ("6")

        self.quitButton.pack()

        playButton.pack()
        stopButton.pack()
        pauseButton.pack()
        wavFormButton.pack()
        
        self.frame.pack()

        print("7")
        
    def close_windows(self):
        self.master.destroy()
    def playSound(self):
        global paused
        paused = False

        self.d1.play()
        print("playing")
    def stopSound(self):
        self.d1.stop()
        print("Stopping")
    def pauseSound(self):
        global paused
        if(paused == False):
            paused = True
            mixer.pause()
            print("pausing")
        else:
            paused = False
            mixer.unpause()
            print("unpausing")
    def waveForm(self):
        
        sampleRate, wavFileDat = scipy.io.wavfile.read(self.fileDirectory)
        plt.plot(wavFileDat)
        print(wavFileDat)
        plt.show()
def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()

