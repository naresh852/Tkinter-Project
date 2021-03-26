from tkinter import *
class colors(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
    def choose(self):
        self.color=StringVar()
        Entry(self,textvariable=self.color,bg="yellow").pack()


    def apply(self):
        self.f1 = Frame(self, bg=self.color.get(), borderwidth=4)
        self.f1.pack(fill="x", side=TOP)
        Button(self.f1, text="apply", command=self.apply).pack()






if __name__=="__main__":
    window=colors()
    window.choose()
    window.apply()
    window.mainloop()

exit()
from tkinter import  *
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x500")
    def status(self):
        self.var1=StringVar()
        self.var1.set("Ready")
        self.var=Label(self,textvar=self.var1,relief=GROOVE,anchor="w")
        self.var.pack(side=BOTTOM,fill=X)
    def click(self):
        print("button clicked")
        self.var1.set("busy..")
        import time
        time.sleep(2)
        self.var1.set("ready now")
        self.geometry("400x200")
    def update(self,btext):
        Button(text=btext,bg="pink",command=self.click).pack()




if __name__=="__main__":
    window=GUI()
    window.status()
    window.update("click me")
    window.mainloop()