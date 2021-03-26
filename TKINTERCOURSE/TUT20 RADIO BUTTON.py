from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as lil
from tkinter import Scale
root=Tk()
def ordered():
    lil.showinfo("ordered",f"your order {var.get()} is placed.Thank you for ordering:)")
    root.quit()
root.title("radio buttons")
root.geometry("400x500")
# var=IntVar()
var=StringVar()
var.set("rabbit")
Label(root,text="what u like to order",font="TimesRoman 14 bold",pady=10).pack(anchor="n")
radio=["dosa","idly","samosa","icecream"]
# for i,item in enumerate(radio):
#     Radiobutton(root,text=item,variable=var,value=item).pack(anchor="w")
# for item in radio:
#     Radiobutton(root,text=item,variable=var,value=radio.index(item)+1).pack(anchor="w")
for item in radio:
    Radiobutton(root,text=item,variable=var,value=item).pack(anchor="w")
Button(root,text="order",command=ordered).pack(anchor="n")
root.mainloop()
