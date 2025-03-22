#program in which user can submit their name 
#TO DISABLE THE ENTRY LABEL USE entry.config(state=DISABLED)
from tkinter import *
def submit():
    get=entry.get()#this function gets whatever is typed in the entry label
    print("HELLO "+ get)
def delete():
    entry.delete(0,END)#deletes everything in the entry label from index 0 to the end of string
def backspace():
    entry.delete(len(entry.get())-1,END)
window=Tk()
entry=Entry(window,font=('Arial',50))
            #show="*")#replaces all the typed letters with * and is useful for password typing)#an entry label lets user type in whatever they want 
entry.pack(side=LEFT)#tells that entry label must be to the left of the screen 
submitbutton=Button(window,
                    text='SUBMIT',
                    command=submit,
                    )
submitbutton.pack(side=RIGHT)
deletebutton=Button(window,
                    text='DELETE',
                    command=delete)
deletebutton.pack(side=RIGHT)
backspacebutton=Button(window,
                       text='BACKSPACE',
                       command=backspace)
backspacebutton.pack(side=TOP)
window.mainloop()