
import re
from tkinter import *
import re
from tkinter.messagebox import*
from functools import reduce
from tkinter import ttk, messagebox


def reset_form():
     code.set("")
     brand.set("")
     name.set("")
     price.set(0)
     quantity.set(0)


#هر سطری در جدول یک کدی دارد رای اینکه زمانی که روش کلیک میکنیم بهش دسترسی داشته باشیم
#از روش زیر استفاده میکنیم
def select_product(event):
     tabel_raw=tabel.focus()
     selected= tabel.item(tabel_raw)['values']
     print(tabel_raw,selected)
     code.set(selected[0])
     brand.set(selected[1])
     name.set(selected[2])
     price.set(selected[3])
     quantity.set(selected[4])



product_list=[]
def save_check():
     product={
          "code":code.get(),
          "brand":brand.get(),
          "name":name.get(),
          "price":price.get(),
          "quantity":quantity.get()
     }
     messagebox.showinfo("Saved",f"Saved successfully! \n{product}")
     reset_form()
     #افزودن تابع جدید به جدول یعنی وقتی سیو و زد بیافته توی جدول
     tabel.insert("",END,values=tuple(product.values()))
def edit_check():
     pass


def remove_check():
     pass
window = Tk()

window.geometry("660x360")
window.title("لطفا مشخصات کالا را وارد کنید")
window.resizable(False, False)

#code
Label(window,text="code").place(x=20,y=20)
code=StringVar()
Entry(window,textvariable=code).place(x=90,y=20)

#brand
Label(window,text="brand").place(x=20,y=60)
brand=StringVar()
Entry(window,textvariable=brand).place(x=90,y=60)


#name
Label(window,text="name").place(x=20,y=100)
name=StringVar()
Entry(window,textvariable=name).place(x=90,y=100)

#price
Label(window,text="price").place(x=20,y=140)
price=IntVar()
Entry(window,textvariable=price).place(x=90,y=140)

#quantity
Label(window,text="quantity").place(x=20,y=180)
quantity=IntVar()
Entry(window,textvariable=quantity).place(x=90,y=180)





Button(window,text="save",width=7,command=save_check).place(x=20,y=300)
Button(window,text="edit",width=7,command=save_check).place(x=90,y=300)
Button(window,text="remove",width=7,command=save_check).place(x=160,y=300)
#tabel
tabel=ttk.Treeview(window,height=12,columns=(1,2,3,4,5),show="headings")
tabel.column(1,width=60)
tabel.column(2,width=90)
tabel.column(3,width=90)
tabel.column(4,width=70)
tabel.column(5,width=70)


#tabel taitel
tabel.heading(1, text="code")
tabel.heading(2, text="brand")
tabel.heading(3, text="name")
tabel.heading(4, text="price")
tabel.heading(5, text="quantity")


#میخواهیم هر زمانی که روی اطلاعات داخل جدول کلیک کرد اطلاعات و داخل لیبل ها نمایش بده
# از رویداد استفاده میکنیمtreeviwselect

tabel.bind("<<TreeviewSelect>>", select_product)

tabel.place(x=250,y=60)
window.mainloop()

