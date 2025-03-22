from tkinter import *
list=['Rock',
'Pop music',
'Popular music',
'Electronic music',
'Country music',
'Hip hop music',
'Rhythm and blues',
'Blues',
'Jazz']

def new():
    window1=Tk()
    songs1=Label(window1,
                 text="ROCK PLAYLIST",
                 font=('Segoe Script',30),
                 bd=10,
                 fg='#fc03e3',
                 bg='black'
                 )
    songs1.pack()
    window1.config(bg='black')
    window1.mainloop()

window = Tk()

titlelabel = Label(window,
                     font=('Segoe Script',30),
                     text='MUSIC PLAYLIST ',
                     #relief=RAISED,
                     bd=10,
                     fg='#fc03e3',
                     bg='black'
                     )



titlelabel.pack()
label1=Label(window,
             padx=20,
             pady=20,
             text='Pick a Genre You Like!',
             font=('Segoe Script',30),
             bd=10,
             fg='#fc03e3',
             bg='black'
             )
label1.pack()

#for i in range(9):
button1=Button(window,
            font=('Segoe Script',13),
            bd=10,
            fg='#fc03e3',
            bg='black',
            command=new,
            text=list[0]
            )
button1.pack(side=LEFT)



"""button2=Button(window,
            font=('Segoe Script',13),
            bd=10,
            fg='#fc03e3',
            bg='black',
            command=display(2),
            text=list[2]
            )
button2.pack(side=LEFT)


button3=Button(window,
            font=('Segoe Script',13),
            bd=10,
            fg='#fc03e3',
            bg='black',
            command=display(3),
            text=list[3]
            )
button3.pack(side=LEFT)"""


window.config(bg='black')
window.mainloop()
