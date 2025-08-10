from tkinter import *
def enter_mouse(event):
    clicked_button = event.widget
    clicked_button.config(background="darkblue",foreground="white")


def exit_mouse(event):
    clicked_button = event.widget
    clicked_button.config(background="lightblue", foreground="black")

def click(event):
    clicked_button = event.widget
    btn_text=clicked_button["text"]
    if btn_text == "C":
        result.set("0")
    if len(result.get())<12:
        if btn_text == "=":
            result.set(round(eval(result.get()), 2))
        elif btn_text in "0123456789":
            result.set(result.get() + btn_text)
        elif btn_text == ".":
            if result.get().count(".")== 0:
                result.set(result.get() + btn_text)
        elif btn_text == "-":
            if result.get().count("-")==0:
                result.set(result.get() + btn_text)
        elif btn_text == "+":
            if result.get().count("+")==0:
                result.set(result.get() + btn_text)
        elif btn_text == "/":
            if result.get().count("/")==0:
                result.set(result.get() + btn_text)
        elif btn_text == "*":
            if result.get().count("*")==0:
                result.set(result.get() + btn_text)
        
        else:
             result.set(result.get() + btn_text)





window = Tk()
window.title("Calculator")
window.geometry("225x240")
labels = [
    ["7", "8", "9", "*"],
    ["4", "5", "6", "/"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"]
]
x_distance = 50
y_distance = 40

x_start = 20
y_start = 70


result=StringVar()
Entry(window,width=14, font=("arial",18),state="readonly",textvariable=result).place(x=20, y=20)
result.set("")
for row in range(4):
    for col in range(4):
        btn = Button(window, text=labels[row][col], font=("arial black", 10), width=3, bg="lightblue",
                     fg="black")
        btn.bind("<Enter>" ,enter_mouse)
        btn.bind("<Leave>" , exit_mouse)
        btn.bind("<Button-1>" ,click)
        btn.place(x=col * x_distance + x_start, y=row * y_distance + y_start)

window.mainloop()
