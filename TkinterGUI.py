# Simple GUI

from tkinter import *

# create the Window
root = Tk()

# modify the root window
root.title("Labeler")
root.geometry("200x200")

app =Frame(root)
app.grid()
button1= Button(app, text="This is button #1")
button1.grid

button2= Button(app, text="This is button #2")
button2.grid

button3= Button(app, text="This is button #3")
button3.grid

# kick-off the event loop
root.mainloop()
