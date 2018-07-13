import random
import time
from tkinter import *
import sqlite3

root =Tk()
root.geometry("1600x800")

root.title("Resturadent Managment System")

Tops =Frame(root,width=1600,height=50,relief=RAISED)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack()

#f2.pack(side=RIGHT)
#---------------DATABASE--------------
table2=sqlite3.connect("Resturdant.db")
#table2.execute('''CREATE TABLE ORDERS(ORDER_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FRIES_MEAL TEXT,LUNCH_MEAL TEXT,BURGER_MEAL TEXT,PIZZA_MEAL TEXT,CHEESE_BURGER TEXT,DRINKS TEXT,COST TEXT,SERVICE_CHARGE TEXT,TAX TEXT,SUBTOTAL TEXT,TOTAL TEXT);''')
#table2.commit()

#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblInfo = Label(Tops,font=('arial',50,'italic','underline','bold'),text="Resturant Managment System",fg='Steel Blue',bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops,font=('arial',20,'italic','bold'),text=localtime,fg='Steel Blue',bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


#lblReference=Label(f1,font=("arial",16,'bold')),text='Referance',bd=16,anchor='w')
#lablReference.grid(row=0,coloumn=0)
def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set(0.0)
    Largefries.set(0.0)
    Burger.set(0.0)
    Filet.set(0.0)
    Subtotal.set(0.0)
    Total.set(0.0)
    Service_Charge.set(0.0)
    Drinks.set(0.0)
    Tax.set(0.0)
    cost.set(0.0)
    Cheese_burger.set(0.0)

rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()
reset()
def billsave():
    cof = float(Fries.get())
    colfries = float(Largefries.get())
    cob = float(Burger.get())
    cofi = float(Filet.get())
    cochee = float(Cheese_burger.get())
    codr = float(Drinks.get())

    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costoffilet = cofi * 50
    costofcheeseburger = cochee * 50
    costofdrinks = codr * 35

    costofmeal = "Rs.", str(
        '%.2f' % (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax = ((costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) * 0.33)
    Totalcost = (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)
    Ser_Charge = (
            (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) / 99)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
    table2.execute(
        "INSERT INTO ORDERS(FRIES_MEAL,LUNCH_MEAL,BURGER_MEAL,PIZZA_MEAL,CHEESE_BURGER,DRINKS,COST,SERVICE_CHARGE,TAX,SUBTOTAL,TOTAL) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (str(costoffries), str(costoflargefries), str(costofburger), str(costoffilet), str(costofcheeseburger),
         str(costofdrinks), str(costofmeal), str(Service), str(PaidTax), str(Totalcost), str(OverAllCost),))
    table2.commit()
    for row in table2.execute("SELECT * FROM ORDERS"):
        print(row)

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="green",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="green",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="green",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="green",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="green",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="green",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="green",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="light green",justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="green",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="green",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="green",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="green",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="light green" ,justify='right')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=18,pady=10, bd=10 ,fg="black",font=('ariel' ,20,'bold'),width=15, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=1, column=7)

btnreset=Button(f1,padx=18,pady=10, bd=10 ,fg="black",font=('ariel' ,20,'bold'),width=15, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=2, column=7)

btnexit=Button(f1,padx=18,pady=10, bd=10 ,fg="black",font=('ariel' ,20,'bold'),width=15, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=3, column=7)

btnbill=Button(f1,padx=18,pady=10, bd=10 ,fg="black",font=('ariel',20,'bold'),width=15, text="SAVE BILL", bg="powder blue",command=billsave)
btnbill.grid(row=4, column=7)


def price():
    roo = Tk()
    roo.geometry("220x220")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'),fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,20,'bold'),width=15, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=5, column=7)

root.mainloop()

