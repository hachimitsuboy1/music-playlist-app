from tkinter import *
from PIL import ImageTk,Image
def click():
    print("YOU CLICKED THE BUTTON")
window=Tk()
photo = ImageTk.PhotoImage(file='C:/Users/sammy/OneDrive/Desktop/68a420bc-4f6e-45e6-9e60-bbab2344555b.jpg')
button = Button(window,
                text="CLICK ME",
                command=click,#lets ypu add functionality to the button
                state=ACTIVE,#state of the button->if its clickable or not
                )
button.pack()
window.mainloop()