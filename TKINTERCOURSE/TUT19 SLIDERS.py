from tkinter import *
import tkinter.messagebox as m
from tkinter import Scale
# def amount():
#     m.showinfo("amount",f"amount {sliders.get()} is credited")
root=Tk()
# root.title("sliders tutorial")
def store():
    with open("records.txt","a") as f:
        f.write(f"{myslider.get()}\n")
    m.showinfo("submit", "Thanks for rating our restaurent :)")
    root.quit()


root.title("rate restaurent")
root.geometry("400x500")

# Label(root,text="how many dollars u want?").pack()
# sliders = Scale(root , from_="0",to="100",orient=HORIZONTAL,tickinterval=50)
# sliders.set(20)
#
# sliders.pack()
# Button(root,text="credit amount",command=amount).pack()
Label(root,text="please give a rating about your experience ").pack()
myslider=Scale(root,from_=1,to=10,orient=HORIZONTAL)
myslider.pack()
Button(root,text="post",command=store).pack()


root.mainloop()