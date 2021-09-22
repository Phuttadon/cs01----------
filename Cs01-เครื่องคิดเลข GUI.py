from tkinter import *
root=Tk()
root.title("เครื่องคิดเลข")
root.geometry("300x300")

content= ""
txt_input = StringVar(value="0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate=float(eval(content))
    txt_input.set(calculate)
    content=""
def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")



#แสดงผล
display = Entry(font=('arial',33,"bold"),fg="white",bg="green",textvariable=txt_input,justify="right")
display.grid(columnspan=4)
root.geometry("500x600")


#รับค่าผ่านปุ่ม

#row1 ปุ่ม 7 8 9 C
btn7=Button(fg="black",font=('arial',30,"bold"),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
btn8=Button(fg="black",font=('arial',30,"bold"),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
btn9=Button(fg="black",font=('arial',30,"bold"),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
btnCl=Button(fg="black",bg='orange',font=('arial',30,"bold"),command=clear,text="C",padx=30,pady=15).grid(row=1,column=3)

#row2 ปุ่ม 4 5 6 +
btn4=Button(fg="black",font=('arial',30,"bold"),text="4",command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
btn5=Button(fg="black",font=('arial',30,"bold"),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
btn6=Button(fg="black",font=('arial',30,"bold"),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
btnPlus=Button(fg="black",bg='orange',font=('arial',30,"bold"),command=lambda:btn("+"),text="+",padx=33,pady=15).grid(row=2,column=3)

#row3 ปุ่ม 1 2 3
btn1=Button(fg="black",font=('arial',30,"bold"),text="1",command=lambda:btn(1),padx=30,pady=15).grid(row=3,column=0)
btn2=Button(fg="black",font=('arial',30,"bold"),text="2",command=lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
btn3=Button(fg="black",font=('arial',30,"bold"),text="3",command=lambda:btn(3),padx=30,pady=15).grid(row=3,column=2)
btnMinus=Button(fg="black",bg='orange',font=('arial',30,"bold"),command=lambda:btn("-"),text="-",padx=38,pady=15).grid(row=3,column=3)

#row4 ปุ่ม * / 0 =
btnX=Button(fg="black",bg='orange',font=('arial',30,"bold"),command=lambda:btn("*"),text="X",padx=27,pady=15).grid(row=4,column=0)
btn0=Button(fg="black",font=('arial',30,"bold"),text="0",command=lambda:btn(0),padx=30,pady=15).grid(row=4,column=1)
btndot=Button(fg="black",bg='orange',font=('arial',30,"bold"),text=".",command=lambda:btn("."),padx=36,pady=15).grid(row=4,column=2)
btnหาร=Button(fg="black",bg='orange',font=('arial',30,"bold"),command=lambda:btn("/"),text="/",padx=39,pady=15).grid(row=4,column=3)

#row5 ปุ่ม =
btnOpen=Button(fg="black",bg='orange',font=('arial',30,"bold"),command=lambda:btn("("),text="(",padx=33,pady=15).grid(row=5,column=0)
btnEqual=Button(fg="black",bg='green',font=('arial',30,"bold"),text="=",command=equal,padx=95,pady=15).grid(row=5,column=1,columnspan=2)
btnClose=Button(fg="black",bg='orange',font=('arial',30,"bold"),command=lambda:btn(")"),text=")",padx=37,pady=15).grid(row=5,column=3)
root.mainloop()