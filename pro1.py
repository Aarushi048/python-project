from tkinter import*
import random
import time
import sqlite3
conn=sqlite3.connect('project.db')

root =Tk()
root.geometry("1600x800")
root.title("Resturadent Managment System")

Tops =Frame(root,width=1600,height=50,relief=RAISED)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#f2=Frame(root,width=400,height=700,bg='blue',relief=SUNKEN)
#f2.pack(side=RIGHT)
localtime=time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops,font=('arial',50,'italic','underline','bold'),text="Resturant Managment System",fg='Steel Blue',bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops,font=('arial',20,'italic','underline','bold'),text=localtime,fg='Steel Blue',bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

#lblReference=Label(f1,font=("arial",16,'bold')),text='Referance',bd=16,anchor='w')
#lablReference.grid(row=0,coloumn=0)

def exit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

def total():


def price():
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable='rand' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Fries' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="blue",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Largefries' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="blue",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Burger' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="blue",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Filet' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="blue",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Cheese_burger' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtCheese_burger.grid(row=5,column=1)


lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="blue",bd=10,anchor='w')
lblDrinks.grid(row=0,column=3)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Drinks' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtDrinks.grid(row=0,column=4)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="blue",bd=10,anchor='w')
lblcost.grid(row=1,column=3)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable='cost' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtcost.grid(row=1,column=4)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="blue",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=3)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Service_Charge' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtService_Charge.grid(row=2,column=4)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="blue",bd=10,anchor='w')
lblTax.grid(row=3,column=3)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Tax' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtTax.grid(row=3,column=4)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="blue",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=3)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable='Subtotal' , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtSubtotal.grid(row=4,column=4)

lblTotal = Label(f1, font=( 'aria',16, 'bold' ),text="Total",fg="blue",bd=10,anchor='w')
lblTotal.grid(row=5,column=3)
txtTotal = Entry(f1,font=('ariel',16,'bold'), textvariable='Total', bd=6,insertwidth=4,bg="light green" ,justify='right')
txtTotal.grid(row=5,column=4)
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel',10,'bold'),width=10, text="TOTAL", bg="light blue",command=total())
btnTotal.grid(row=1, column=6)
btnprice=Button(f1,padx=16,pady=8, bd=10,fg="black",font=('ariel',10,'bold'),width=10, text="PRICE", bg="light blue",command=price())
btnprice.grid(row=2, column=6)
btnreset=Button(f1,padx=16,pady=8, bd=10,fg="black",font=('ariel',10,'bold'),width=10, text="RESET", bg="light blue",command=reset())
btnreset.grid(row=3, column=6)
btnext=Button(f1,padx=16,pady=8, bd=10,fg="black",font=('ariel',10,'bold'),width=10,text="EXIT", bg="light blue",command=exit())
btnext.grid(row=4, column=6)
mainloop()