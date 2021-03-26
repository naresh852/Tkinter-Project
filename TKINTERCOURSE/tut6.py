from tkinter import *
from PIL import Image,ImageTk
naresh=Tk()
# gui attributes of label
# font="Timesroman 12 italic"
# font=("TimesRoman" "15" "bold")
naresh.geometry("700x500")
title_label=Label(text='''In 1976, if you had told fourteen-year-old Franciscan seminary student Thomas Cruise Mapother IV 
                      \n that one day in the not too distant future he would be Tom Cruise, one of the top 100 movie
                        \nstars of all time, he would have probably grinned and told you that his ambition was to join
                        \nthe priesthood. Nonetheless, this sensitive, deeply religious youngster who was born in 1962 in Syracuse,
                  \nNew York, was destined to become one of the highest paid and most sought after actors in screen history''',bg="red",
                  fg="white",padx=20,pady=200,font=("TimesRoman" "15" "bold"),borderwidth=10,relief=GROOVE)
# title_label.pack(side="bottom",anchor="se",fill="x")
title_label.pack(side="left",fill="y",padx="100",pady="50")

naresh.mainloop()