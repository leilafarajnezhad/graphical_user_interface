import re
from tkinter import *
import re
from tkinter.messagebox import*
from functools import reduce
product_list=[]
def name_validator(name):
     if re.match(r"^[a-zA-Z\s]{3,30}$",name):
          return True
     else:
          return False
def calculate_total_price():
    # مجموع price × count با استفاده از reduce
    return reduce(lambda total, item: total + item["price"] * item["count"], product_list, 0)

def save_check():
     if name_validator(name.get())and  1<count.get() < 10 and 0<price.get() < 1000:
          product = {"name": name.get(), "count": count.get(), "price": price.get()}
          product_list.append(product)
          print(product_list)
          name.set("")
          count.set(1)
          price.set(0)
          showinfo("save","success")
          total.set(f"Total price={calculate_total_price()}")
     else:
          showerror("error","not a valid name/count/price")
window = Tk()

window.geometry("600x300")
window.title("لطفا مشخصات کالا را وارد کنید")

Label(window,text="name:").place(x=20,y=20)
name = StringVar()
Entry(window,textvariable=name).place(x=20,y=40)

Label(window,text="count:").place(x=20,y=60)
count = IntVar()
Entry(window,textvariable=count).place(x=20,y=80)

Label(window,text="price:").place(x=20,y=100)
price = IntVar()
Entry(window,textvariable=price).place(x=20,y=120)

total = StringVar(value= "Total=0")
Label(window,textvariable=total,font=("Aria",20)).place(x=20,y=140)



Button(window,text="save",width=10,command=save_check).place(x=20,y=200)

window.mainloop()

