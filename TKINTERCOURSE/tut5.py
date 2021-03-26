from tkinter import *
from PIL import Image,ImageTk
naresh=Tk()
naresh.geometry("1592x1236")
# first opoen iamge
image=Image.open("1.jpg")
# convert to Tk
image1=ImageTk.PhotoImage(image)
# addd a Label
narLabel=Label(image=image1)
narLabel.pack()

naresh.mainloop()