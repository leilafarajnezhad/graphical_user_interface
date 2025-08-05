import re
from tkinter import *
import re
from tkinter.messagebox import*
from functools import reduce
from tkinter import ttk, messagebox

def enter_function(event_info):
    my_label.config(background="black")

def exit_function(event_info):
    my_label.config(background="white")

calculator=Tk()


calculator.geometry('320x400')
calculator.title('Calculator')

Entry(calculator,width=45).place(x=20, y=40,height=90)

my_label= Button(calculator,text="7",width=4)
my_label.place(x=20,y=140)
my_label.bind("<Enter>",enter_function)
my_label.bind("<Leave>",exit_function)
Button(calculator,text="8",width=4).place(x=80,y=140)
Button(calculator,text="9",width=4).place(x=140,y=140)
Button(calculator,text="/",width=4).place(x=200,y=140)
Button(calculator,text="%",width=4).place(x=260,y=140)
Button(calculator,text="4",width=4).place(x=20,y=200)
Button(calculator,text="5",width=4).place(x=80,y=200)
Button(calculator,text="6",width=4).place(x=140,y=200)
Button(calculator,text="*",width=4).place(x=200,y=200)
Button(calculator,text="1/x",width=4).place(x=260,y=200)
Button(calculator,text="1",width=4).place(x=20,y=260)
Button(calculator,text="2",width=4).place(x=80,y=260)
Button(calculator,text="3",width=4).place(x=140,y=260)
Button(calculator,text="-",width=4).place(x=200,y=260)
Button(calculator,text="=",width=4,height=5).place(x=260,y=260)
Button(calculator,text="0",width=12).place(x=20,y=320)
Button(calculator,text=".",width=4).place(x=140,y=320)
Button(calculator,text="+",width=4).place(x=200,y=320)



calculator.mainloop()

