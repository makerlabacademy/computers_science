from functions import *
from tkinter import *
w = Tk()
w.title("Drone Controller")
w.geometry("1000x600")
bgImage = PhotoImage(file="images/bg.png")
l = Label(image=bgImage)
l.place(x=0, y=0)
#Upload Buttons Images
rightimg = PhotoImage(file="images/right.png")
leftimg = PhotoImage(file="images/left.png")
upimg = PhotoImage(file="images/up.png")
downimg = PhotoImage(file="images/down.png")
#Create Buttons
btnRight = Button(image=rightimg, command=moveRight)
btnLeft = Button(image=leftimg, command=moveLeft)
btnUp = Button(image=upimg, command=moveForward())
btnDown = Button(image=downimg, command=moveBack)
#Place the Buttons
btnRight.place(x=533, y=255)
btnLeft.place(x=197, y=255)
btnUp.place(x=365, y=127)
btnDown.place(x=365, y=405)
w.mainloop()
