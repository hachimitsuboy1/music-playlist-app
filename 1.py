from tkinter import *
window = Tk()#initializes a window
window.config(background="black")
window.title("MY FIRST GUI")
photo = PhotoImage(file='C:\Users\sammy\OneDrive\Desktop\Wallpaper\1447881261-4845a3f3a232efe6ff5712e8058a5e6e.png')#adds the file in the file path mentioned as a photo image
label=Label(window,#tells that window is the master of this label 
            text="HELLO WORLD",
            font=("Arial",40,"bold"),
            bg="black",#background color
            fg="green",#foreground color
            relief=RAISED,#border
            bd=10,#border thickness
            padx=20,
            pady=20,#distance between the text and the border
            image=photo,
            compund="top"#tells that image should be on the top 

            )
label.pack()#displays the label in the speicified window
window.mainloop()#displays the window
