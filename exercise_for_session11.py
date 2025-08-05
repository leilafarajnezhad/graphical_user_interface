
import re
from tkinter import *
import re
from tkinter.messagebox import*
from functools import reduce
from tkinter import ttk, messagebox



def number_validator(number):
     if re.match(r"^\d{4}-\d{3}-\d{4]$", number):
          return True
     else:
          return False


def family_owner(owner):
     if re.match(r"^[A-Za-z\s]{3,30}$", owner):
          return True
     else:
          return False


def operator_ckeck(operator):
     if re.match(r"^[A-Za-z\s]{3,30}$", operator):
          return True
     else:
          return False
def charge_check():
     if 1 <charge_check<500000:
          return True
     else:
          print("not enough charge")
          return False


def reset_form():
     number.set(0)
     owner.set("")
     operator.set("")
     charge.set(0)
     register_data.set(0)


#هر سطری در جدول یک کدی دارد رای اینکه زمانی که روش کلیک میکنیم بهش دسترسی داشته باشیم
#از روش زیر استفاده میکنیم
def select_product(event):
     tabel_raw=tabel.focus()
     selected= tabel.item(tabel_raw)['values']
     print(tabel_raw,selected)
     number.set(selected[0])
     owner.set(selected[1])
     operator.set(selected[2])
     charge.set(selected[3])
     register_data.set(selected[4])



product_list=[]

def save_check():
   if number_validator(number.get()) and family_owner(owner.get())and operator_ckeck(operator.get()):
     product={
          "number":number.get(),
          "owner":owner.get(),
          "operator":operator.get(),
          "charge":charge.get(),
          "registerdata":register_data.get()
     }
     product_list.append(product)
     print(product_list)
     messagebox.showinfo("Saved",f"Saved successfully! \n{product}")
     reset_form()
     #افزودن تابع جدید به جدول یعنی وقتی سیو و زد بیافته توی جدول
     tabel.insert("",END,values=tuple(product.values()))
def edit_check():
     pass


def remove_check():
     pass
window = Tk()

window.geometry("680x360")
window.title("لطفا مشخصات کالا را وارد کنید")
window.resizable(False, False)

#number
Label(window,text="number").place(x=20,y=20)
number=IntVar()
Entry(window,textvariable=number).place(x=95,y=20)

#owner
Label(window,text="owner").place(x=20,y=60)
owner=StringVar()
Entry(window,textvariable=owner).place(x=95,y=60)


#operator
Label(window,text="operator").place(x=20,y=100)
operator=StringVar()
Entry(window,textvariable=operator).place(x=95,y=100)

#chargecharge
Label(window,text="charge").place(x=20,y=140)
charge=IntVar()
Entry(window,textvariable=charge).place(x=95,y=140)

#register_data
Label(window,text="register_data").place(x=20,y=180)
register_data=IntVar(value="00/00/00")
Entry(window,textvariable=register_data).place(x=95,y=180)





Button(window,text="save",width=7,command=save_check).place(x=20,y=300)
Button(window,text="edit",width=7,command=save_check).place(x=90,y=300)
Button(window,text="remove",width=7,command=save_check).place(x=160,y=300)
#tabel
tabel=ttk.Treeview(window,height=12,columns=(1,2,3,4,5),show="headings")
tabel.column(1,width=60)
tabel.column(2,width=90)
tabel.column(3,width=90)
tabel.column(4,width=70)
tabel.column(5,width=90)


#tabel taitel
tabel.heading(1, text="number")
tabel.heading(2, text="owner")
tabel.heading(3, text="operator")
tabel.heading(4, text="charge")
tabel.heading(5, text="register_data")


#میخواهیم هر زمانی که روی اطلاعات داخل جدول کلیک کرد اطلاعات و داخل لیبل ها نمایش بده
# از رویداد استفاده میکنیمtreeviwselect

tabel.bind("<<TreeviewSelect>>", select_product)

tabel.place(x=250,y=60)
window.mainloop()

