from tkinter import *
from PIL import Image,ImageTk
root=Tk()
canvas_width=600
canvas_height=500
root.title("naresh apk")
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
# line goes from x1,y1 to x2,y2
can_widget.create_line(0,0,600,500,fill="blue")
can_widget.create_text(260,200,text="hello bitch")
can_widget.create_rectangle(100,100,400,400,fill="red")
can_widget.create_oval(100,100,400,400,fill="white")
img=Image.open("1.jpg")
img1=PhotoImage(file="bike.png")
img2=ImageTk.PhotoImage(img)
can_widget.create_image(10,50,anchor=NW,image=img1)
root.mainloop()