from tkinter import *
root=Tk()
root.title("เครื่องคิดเลข")
myText= Label(text="My name is ",fg="blue",font=20).grid(row=0,column=0)
myText= Label(text="Phuttadon",fg="red",font=20).grid(row=1,column=1)
myText= Label(text="นะจ๊ะ",fg="green",font=20).grid(row=3,column=2)
root.geometry("300x300")
root.mainloop()