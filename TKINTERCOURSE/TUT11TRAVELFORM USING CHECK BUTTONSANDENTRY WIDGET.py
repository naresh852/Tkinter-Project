from tkinter import *
root=Tk()

root.geometry("400x500")
def getval():
    print("its working")

Label(text="welcome to canteen",font="sans-serif 15 bold",pady="10",bg="yellow").grid(row=0,column=3)
Label(text="name").grid(row=1,column=0)
Label(text="number").grid(row=2,column=0)
Label(text="gender").grid(row=3,column=0)
Label(text="age").grid(row=4,column=0)
Label(text="mealname").grid(row=5,column=0)
# entry names variables
nameentry=StringVar()
numberentry=StringVar()
genderentry=StringVar()
ageentry=StringVar()
mealnameentry=StringVar()
foodorder=IntVar()
# add entryes
Entry(textvariable=nameentry).grid(row=1,column=3)
Entry(textvariable=numberentry).grid(row=2,column=3)
Entry(textvariable=genderentry).grid(row=3,column=3)
Entry(textvariable=ageentry).grid(row=4,column=3)
Entry(textvariable=mealnameentry).grid(row=5,column=3)
# checkbutton and pack
Checkbutton(text="book now",variable=foodorder).grid(row=6,column=3)
# sunbit button and grid
Button(text="submit",command=getval).grid(row=7,column=3)
root.mainloop()