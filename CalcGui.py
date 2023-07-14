from tkinter import *
Form1 = Tk() 
Form1.geometry('237x300')
Form1.resizable(False, False)
Edit = Entry(Form1, width='35', borderwidth=3)#
Edit.grid(row= 0 , column=0, padx=10, pady=10)
def Button_Do(number):
    current = Edit.get()
    Edit.delete(0, END)
    Edit.insert(0, str(current) + str(number))
    
def Button_Clear():
    Edit.delete(0, END)
    
def Button_N():
    first = Edit.get()
    global fn
    global mod
    mod = 2
    Edit.delete(0, END)
    fn = int(first)

def Button_Z():
    first = Edit.get()
    global fn
    global mod
    mod = 1
    Edit.delete(0, END)
    fn = int(first)
    
def Button_D():
    first = Edit.get()
    global fn
    global mod
    mod = 3
    Edit.delete(0, END)
    fn = int(first)
    
def Button_K():
    first = Edit.get()
    global fn
    global mod
    mod = 4
    Edit.delete(0, END)
    fn = int(first)
    
def Button_Y():
    second = Edit.get()
    Edit.delete(0, END)    
    if mod == 1 : Edit.insert(0 , fn + int(second))
    elif mod == 2 : Edit.insert(0 , fn - int(second))
    elif mod == 3 : Edit.insert(0 , fn * int(second))
    elif mod == 4 : Edit.insert(0 , fn / int(second))
    return

Button_7 = Button(Form1, text='7', command=lambda: Button_Do("7"), padx=20, pady=5).place(x=10, y=55)
Button_8 = Button(Form1, text='8', command=lambda: Button_Do("8"), padx=20, pady=5).place(x=65, y=55)
Button_9 = Button(Form1, text='9', command=lambda: Button_Do("9"), padx=20, pady=5).place(x=120, y=55)
Button_K = Button(Form1, text='/', command=Button_K,  padx=20, pady=5).place(x=175, y=55)
Button_4 = Button(Form1, text='4', command=lambda: Button_Do("4"), padx=20, pady=5).place(x=10, y=90)
Button_5 = Button(Form1, text='5', command=lambda: Button_Do("5"), padx=20, pady=5).place(x=65, y=90)
Button_6 = Button(Form1, text='6', command=lambda: Button_Do("6"), padx=20, pady=5).place(x=120, y=90)
Button_D = Button(Form1, text='*', command=Button_D,  padx=20, pady=5).place(x=175, y=90)
Button_1 = Button(Form1, text='1', command=lambda: Button_Do("1"), padx=20, pady=5).place(x=10, y=125)
Button_2 = Button(Form1, text='2', command=lambda: Button_Do("2"), padx=20, pady=5).place(x=65, y=125)
Button_3 = Button(Form1, text='3', command=lambda: Button_Do("3"), padx=20, pady=5).place(x=120, y=125)
Button_N = Button(Form1, text='-', command=Button_N , padx=20, pady=5).place(x=175, y=125)
Button_0 = Button(Form1, text='0', command=lambda: Button_Do("0"), padx=20, pady=5).place(x=10, y=160)
Button_F = Button(Form1, text=',',  padx=21, pady=5).place(x=65, y=160)
Button_Y = Button(Form1, text='=', command=Button_Y, padx=19, pady=5).place(x=120, y=160)
Button_Z = Button(Form1, text='+', command=Button_Z, padx=19, pady=5).place(x=175, y=160)
Button_clear = Button(Form1, text='Clear', command=Button_Clear, padx=37, pady=5).place(x=10, y=195)

Form1.mainloop()



