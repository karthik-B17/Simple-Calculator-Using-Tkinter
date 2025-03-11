import tkinter.messagebox
from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry("500x500")
e_b=Entry(window,width=75,borderwidth=15)
e_b.focus()
e_b.place(x=0,y=0)
#command
def click(num):
    res=e_b.get()
    e_b.delete(0,END)
    e_b.insert(0,str(res)+str(num))
def clearall_():
        e_b.delete(0,END)
def backspace():
    current_text = e_b.get()
    if len(current_text) > 0:
        e_b.delete(len(current_text) - 1, END)
def powoff():
    m= tkinter.messagebox.askyesno('Exit','Do You Want to Exit?')
    if m == True:
      window.destroy()
    elif m == False:
       return 1


button=Button(window,text='Power off',width=15,borderwidth=15,command=powoff)
button.place(x=10,y=60)
button=Button(window,text='BackSpace',width=15,borderwidth=15,command=backspace)
button.place(x=350,y=60)
button=Button(window,text='1',width=15,borderwidth=15,command=lambda: click(1))
button.place(x=10,y=120)
button=Button(window,text='2',width=15,borderwidth=15,command=lambda: click(2))
button.place(x=180,y=120)
button=Button(window,text='3',width=15,borderwidth=15,command=lambda: click(3))
button.place(x=350,y=120)
button=Button(window,text='4',width=15,borderwidth=15,command=lambda: click(4))
button.place(x=10,y=180)
button=Button(window,text='5',width=15,borderwidth=15,command=lambda: click(5))
button.place(x=180,y=180)
button=Button(window,text='6',width=15,borderwidth=15,command=lambda: click(6))
button.place(x=350,y=180)
button=Button(window,text='7',width=15,borderwidth=15,command=lambda: click(7))
button.place(x=10,y=240)
button=Button(window,text='8',width=15,borderwidth=15,command=lambda: click(8))
button.place(x=180,y=240)
button=Button(window,text='9',width=15,borderwidth=15,command=lambda: click(9))
button.place(x=350,y=240)
button=Button(window,text='AC',width=15,borderwidth=15,command=clearall_)
button.place(x=10,y=300)
button=Button(window,text='0',width=15,borderwidth=15,command=lambda: click(0))
button.place(x=180,y=300)
#operators
def add():
    n1=e_b.get()
    global math
    global i
    math='+'
    i=int(n1)
    e_b.delete(0,END)
button=Button(window,text='+',width=15,borderwidth=15,command=add)
button.place(x=10,y=360)
def sub():
    n1=e_b.get()
    global math
    global i
    math='-'
    i=int(n1)
    e_b.delete(0,END)
button=Button(window,text='-',width=15,borderwidth=15,command=sub)
button.place(x=180,y=360)
def mul():
    n1=e_b.get()
    global math
    global i
    math='*'
    i=int(n1)
    e_b.delete(0,END)
button=Button(window,text='*',width=15,borderwidth=15,command=mul)
button.place(x=350,y=360)
def div():
    n1=e_b.get()
    global math
    global i
    math='/'
    i=int(n1)
    e_b.delete(0,END)
button=Button(window,text='/',width=15,borderwidth=15,command=div)
button.place(x=10,y=420)
def eql():
    n2=e_b.get()
    e_b.delete(0,END)
    if math=='+':
         e_b.insert(0,i + int(n2))
    elif math=='-':
        e_b.insert(0,i - int(n2))
    elif math=='*':
        e_b.insert(0,i * int(n2))
    elif math=='/':
         e_b.insert(0,i / int(n2))
    else:
        e_b.insert(0,0)
button=Button(window,text='=',width=15,borderwidth=15,command=eql)
button.place(x=350,y=300)
window.mainloop()


