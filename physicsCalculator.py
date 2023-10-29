from tkinter import *

root = Tk()
root.title="Calculator"
e=Entry(root,width=35,borderwidth=5)
e.grid(row=1,column=0,columnspan=4,padx=10,pady=10)

def button_click(number):
    current =e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_add():
    c=e.get()
    global x 
    global math 
    math = "addition"
    x = float(c)
    e.delete(0,END)
    
def button_equal():
    if math == "addition":
        second = e.get()
        e.delete(0,END)
        e.insert(0,float(second)+x)
    if math == "subract":
        second = e.get()
        e.delete(0,END)
        e.insert(0,x-float(second))
    if math == "multiply":
        second = e.get()
        e.delete(0,END)
        e.insert(0,x*float(second))
    if math == "divide":
        second = e.get()
        e.delete(0,END) 
        e.insert(0,x/float(second))
    if math == "density":
        second = e.get()
        e.delete(0,END)
        third = f.get()
        e.insert(0,float(second)/float(third))
        f.destroy()
        mylabel.destroy()
        my.destroy()
    if math == "acc":
        second = e.get()
        e.delete(0,END)
        third = f.get()
        fourth = g.get()
        e.insert(0,(float(second)-float(third))/float(fourth))
        f.destroy()
        g.destroy()
        mylabel.destroy()
        my.destroy()
        my2.destroy()
    if math == "pressure":
        second = e.get()
        e.delete(0,END)
        third = f.get()
        e.insert(0,float(second)/float(third))
        f.destroy()
        mylabel.destroy()
        my.destroy()
    if math == "force":
        second = e.get()
        e.delete(0,END)
        third = f.get()
        e.insert(0,float(second)*float(third))
        f.destroy()
        mylabel.destroy()
        my.destroy()
    if math == "work":
        second = e.get()
        e.delete(0,END)
        third = f.get()
        e.insert(0,float(second)*float(third))
        f.destroy()
        mylabel.destroy()
        my.destroy()
        
        

def button_subract():
    c=e.get()
    global x
    global math 
    math = "subract"
    x = float(c)
    e.delete(0,END)
    
    

def button_multiply():
    c=e.get()
    global x 
    global math 
    math = "multiply"
    x = float(c)
    e.delete(0,END)
    

def button_divide():
    c=e.get()
    global x 
    global math 
    math = "divide"
    x = float(c)
    e.delete(0,END)
    

def button_density():
    global f
    global mylabel
    global my 
    mylabel = Label(root, text="Enter mass:")
    mylabel.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
    my = Label(root,text="Enter volume:")
    my.grid(row=2,column=0,columnspan=4,padx=10,pady=10)
    f=Entry(root,width=35,borderwidth=5)
    f.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
    global math 
    math = "density"
    
def button_acceleration():
    global f
    global mylabel
    global my 
    global my2
    global g
    mylabel = Label(root, text="final speed")
    mylabel.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
    my = Label(root,text="inital speed")
    my.grid(row=2,column=0,columnspan=4,padx=10,pady=10)
    my2 = Label(root,text="time")
    my2.grid(row=4,column=0,columnspan=4,padx=10,pady=10)
    f=Entry(root,width=35,borderwidth=5)
    f.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
    g=Entry(root,width=35,borderwidth=5)
    g.grid(row=5,column=0,columnspan=4,padx=10,pady=10)
    global math 
    math = "acc"
    
def button_pressure():
    global f
    global mylabel
    global my 
    mylabel = Label(root, text="Enter force")
    mylabel.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
    my = Label(root,text="Enter area")
    my.grid(row=2,column=0,columnspan=4,padx=10,pady=10)
    f=Entry(root,width=35,borderwidth=5)
    f.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
    global math 
    math = "pressure"
    
def button_force():
    global f
    global mylabel
    global my 
    mylabel = Label(root, text="Enter mass")
    mylabel.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
    my = Label(root,text="Enter acceleration")
    my.grid(row=2,column=0,columnspan=4,padx=10,pady=10)
    f=Entry(root,width=35,borderwidth=5)
    f.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
    global math 
    math = "force"
def button_work():
    global f
    global mylabel
    global my 
    mylabel = Label(root, text="Enter force")
    mylabel.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
    my = Label(root,text="Enter distance")
    my.grid(row=2,column=0,columnspan=4,padx=10,pady=10)
    f=Entry(root,width=35,borderwidth=5)
    f.grid(row=3,column=0,columnspan=4,padx=10,pady=10)
    global math 
    math = "work"
  
buttonwork = Button(root,text="Work",padx=20,pady=20,command=button_work)
buttonforce = Button(root,text="Force",padx=20,pady=20,command=button_force)
buttonpressure= Button(root,text="Pressure",padx=20,pady=20,command=button_pressure)
buttondensity = Button(root,text="Density",padx=20,pady=20,command=button_density)
button_acc = Button(root,text="Acceleration",padx=20,pady=20,command=button_acceleration)
button_1 = Button(root,text="1",padx=30,pady=20,command =lambda: button_click(1))
button_2 = Button(root,text="2",padx=30,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=30,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=30,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=30,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=30,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=30,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=30,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=30,pady=20,command=lambda:button_click(9))
button_0 = Button(root,text="0",padx=30,pady=20,command=lambda:button_click(0))
buttonadd = Button(root,text ="+",padx=30,pady=20,command=button_add)
buttonequal = Button(root,text ="=",padx=91,pady=20,command=button_equal)
buttonclear = Button(root,text ="Clear",padx=79,pady=20,command=lambda:button_clear())
button_subract = Button(root,text ="-",padx=30,pady=20,command=button_subract)
button_multiply = Button(root,text ="*",padx=30,pady=20,command=button_multiply)
button_divide = Button(root,text ="/",padx=30,pady=20,command=button_divide)
button_quit= Button(root,text="Exit",padx=30,pady=20,command=root.quit)

button_1.grid(row=8,column=0)
button_2.grid(row=8,column=1)
button_3.grid(row=8,column=2)

button_4.grid(row=7,column=0)
button_5.grid(row=7,column=1)
button_6.grid(row=7,column=2)

button_7.grid(row=6,column=0)
button_8.grid(row=6,column=1)
button_9.grid(row=6,column=2)

button_0.grid(row=9,column=0)
buttonclear.grid(row=9,column=1,columnspan=2)
buttonadd.grid(row=10,column=0)
buttonequal.grid(row=10,column=1,columnspan=2)

button_subract.grid(row=11,column=0)
button_multiply.grid(row=11,column=1)
button_divide.grid(row=11,column=2)

buttonwork.grid(row=10,column=3)
buttonforce.grid(row=9,column=3)
buttonpressure.grid(row=8,column=3)
button_quit.grid(row=11,column=3)
buttondensity.grid(row=6,column=3)
button_acc.grid(row=7,column=3)
# padx for horizontal stretch and pady for vertical stretch 
#fg for foreground color and command to call the function the button will operate
root.mainloop()