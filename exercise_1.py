from tkinter import *

peron_list=[]
def save_check():
     person={"name":name.get,"age":age.get,"family":family.get}
     peron_list.append(person)
     print(peron_list)
     name.set("")
     family.set("")
     age.set(0)
window = Tk()

window.geometry("600x300")
window.title("لطفا مشخصات فردی خود را وارد کنید")

Label(window,text="name:").place(x=20,y=20)
name = StringVar()
Entry(window,textvariable=name).place(x=20,y=40)

Label(window,text="family:").place(x=20,y=60)
family = StringVar()
Entry(window,textvariable=family).place(x=20,y=80)

Label(window,text="age:").place(x=20,y=100)
age = IntVar()
Entry(window,textvariable=age).place(x=20,y=120)

Button(window,text="save",width=10,command=save_check).place(x=20,y=140)

window.mainloop()

