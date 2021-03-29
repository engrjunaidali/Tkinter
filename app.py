from tkinter import *
from tkinter import messagebox as mb

Window = Tk()

Window.title("Hy")
Window.geometry('350x200')

def click():
    mb.showinfo("Button was clicked")


l1 = Label(Window, text="Hello",font=("Calibiri Detail Bold",30)).grid(row=0,column=1)

btn=Button(Window,text="Click Here",width=30,bg="Blue",fg="White")
btn.grid(row=1,column=1)

txt1=Entry(Window)
txt1.grid(row=2,column=1)

# Set Focus
txt2=Entry(Window)
txt2.grid(row=3,column=1)

txt2.focus()

# Disable Entry

txt3=Entry(Window,width=10,state="disabled")
txt3.grid(row=4,column=1)

# Add a combobox
from tkinter.ttk import *
combo1 = Combobox(Window)
combo1.grid(row=6,column=1)
combo1["values"]=(1,2,3,4,5,"Text")



Window.mainloop()