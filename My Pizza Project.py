from tkinter import *
from tkinter import messagebox
import time
import datetime
import random
import ast


root =Tk()
root.geometry("1450x750")
root.title("The Pizza House")
root.configure(background='#90ee90',pady=20)

Tops = Frame(root,bg='crimson',bd=15,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('lucida handwriting',50,'bold'),text='The Pizza House  ',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='#ea3c53',bd=7,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT,padx=30)

Buttons_F=Frame(ReceiptCal_F,bg='green',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='#ea3c53',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='green',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='#ea3c53',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT,padx=30)

Cost_F=Frame(MenuFrame,bg='cornsilk',bd=4)
Cost_F.pack(side=BOTTOM)
Cost_F.configure(padx=193)
Drinks_F=Frame(MenuFrame,bg='#03c03c',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='#ea3c53',bd=4,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='#ea3c53',bd=4,relief=RIDGE)
Food_F.configure(pady=7)
Food_F.pack(side=RIGHT)

#variables#

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Sprite = StringVar()
E_Pepsi = StringVar()
E_DietCoke = StringVar()
E_Mojito = StringVar()
E_Cappuccino = StringVar()
E_Fanta = StringVar()
E_CocaCola = StringVar()
E_ColdCoffee = StringVar()

E_Cheese_N_Corn = StringVar()
E_African_peri_peri_veg = StringVar()
E_Margherita = StringVar()
E_Deluxe_Veggie = StringVar()
E_Veg_Extravaganza = StringVar()
E_Peppy_Paneer = StringVar()
E_Indi_Tandoori_paneer = StringVar()
E_Mexican_Green_Wave = StringVar()

E_Sprite.set("0")
E_Pepsi.set("0")
E_DietCoke.set("0")
E_Mojito.set("0")
E_Cappuccino.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_ColdCoffee.set("0")

E_Cheese_N_Corn.set("0")
E_African_peri_peri_veg.set("0")
E_Margherita.set("0")
E_Deluxe_Veggie.set("0")
E_Veg_Extravaganza.set("0")
E_Peppy_Paneer.set("0")
E_Indi_Tandoori_paneer.set("0")
E_Mexican_Green_Wave.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

#Function Declaration#

def iExit():
    response = messagebox.showinfo("Thank You", "Thank you for visiting The Pizza House!\nWe hope to see you again soon!")
    if response == 'ok':
        root.destroy()

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_DietCoke.set("0")
    E_Mojito.set("0")
    E_Cappuccino.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_ColdCoffee.set("0")

    E_Cheese_N_Corn.set("0")
    E_African_peri_peri_veg.set("0")
    E_Margherita.set("0")
    E_Deluxe_Veggie.set("0")
    E_Veg_Extravaganza.set("0")
    E_Peppy_Paneer.set("0")
    E_Indi_Tandoori_paneer.set("0")
    E_Mexican_Green_Wave.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtSprite.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtDietCoke.configure(state=DISABLED)
    txtMojito.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtCheese_N_Corn.configure(state=DISABLED)
    txtAfrican_peri_peri_veg.configure(state=DISABLED)
    txtMargherita.configure(state=DISABLED)
    txtDeluxe_Veggie.configure(state=DISABLED)
    txtVeg_Extravaganza.configure(state=DISABLED)
    txtPeppy_Paneer.configure(state=DISABLED)
    txtIndi_Tandoori_paneer.configure(state=DISABLED)
    txtMexican_Green_Wave.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Sprite.get())
    Item2=float(E_Pepsi.get())
    Item3=float(E_DietCoke.get())
    Item4=float(E_Mojito.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_Fanta.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_ColdCoffee.get())

    Item9=float(E_Cheese_N_Corn.get())
    Item10=float(E_African_peri_peri_veg.get())
    Item11=float(E_Margherita.get())
    Item12=float(E_Deluxe_Veggie.get())
    Item13=float(E_Veg_Extravaganza.get())
    Item14=float(E_Peppy_Paneer.get())
    Item15=float(E_Indi_Tandoori_paneer.get())
    Item16=float(E_Mexican_Green_Wave.get())

    PriceofDrinks =(Item1 * 65) + (Item2 * 75) + (Item3 * 99) + (Item4 * 90) + (Item5 * 150) + (Item6 * 75) + (Item7 * 75) + (Item8 * 89)
    PriceofFood =(Item9 * 300) + (Item10 * 175) + (Item11 * 255) + (Item12 * 480) + (Item13 * 240) + (Item14 * 300) + (Item15 * 340) + (Item16 * 213)

    DrinksPrice = "Rs",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "Rs",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)

    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofFood))
    TotalCost.set(TC)


def chkSprite():
    if(var1.get() == 1):
        txtSprite.configure(state = NORMAL)
        txtSprite.focus()
        txtSprite.delete('0',END)
        E_Sprite.set('')
    elif(var1.get() == 0):
        txtSprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chkPepsi():
    if(var2.get() == 1):
        txtPepsi.configure(state = NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0',END)
        E_Pepsi.set("")
    elif(var2.get() == 0):
        txtPepsi.configure(state = DISABLED)
        E_Pepsi.set("0")

def chk_DietCoke():
    if(var3.get() == 1):
        txtDietCoke.configure(state = NORMAL)
        txtDietCoke.delete('0',END)
        txtDietCoke.focus()
    elif(var3.get() == 0):
        txtDietCoke.configure(state = DISABLED)
        E_DietCoke.set("0")

def chk_Mojito():
    if(var4.get() == 1):
        txtMojito.configure(state = NORMAL)
        txtMojito.delete('0',END)
        txtMojito.focus()
    elif(var4.get() == 0):
        txtMojito.configure(state = DISABLED)
        E_Mojito.set("0")

def chk_Cappuccino():
    if(var5.get() == 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.delete('0',END)
        txtCappuccino.focus()
    elif(var5.get() == 0):
        txtCappuccino.configure(state = DISABLED)
        E_Cappuccino.set("0")

def chk_Fanta():
    if(var6.get() == 1):
        txtFanta.configure(state = NORMAL)
        txtFanta.delete('0',END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state = DISABLED)
        E_Fanta.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_ColdCoffee():
    if(var8.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        txtColdCoffee.delete('0',END)
        txtColdCoffee.focus()
    elif(var8.get() == 0):
        txtColdCoffee.configure(state = DISABLED)
        E_ColdCoffee.set("0")

def chk_Cheese_N_Corn():
    if(var9.get() == 1):
        txtCheese_N_Corn.configure(state = NORMAL)
        txtCheese_N_Corn.delete('0',END)
        txtCheese_N_Corn.focus()
    elif(var9.get() == 0):
        txtCheese_N_Corn.configure(state = DISABLED)
        E_Cheese_N_Corn.set("0")

def chk_African_peri_peri_veg():
    if(var10.get() == 1):
        txtAfrican_peri_peri_veg.configure(state = NORMAL)
        txtAfrican_peri_peri_veg.delete('0',END)
        txtAfrican_peri_peri_veg.focus()
    elif(var10.get() == 0):
        txtAfrican_peri_peri_veg.configure(state = DISABLED)
        E_African_peri_peri_veg.set("0")

def chk_Margherita():
    if(var11.get() == 1):
        txtMargherita.configure(state = NORMAL)
        txtMargherita.delete('0',END)
        txtMargherita.focus()
    elif(var11.get() == 0):
        txtMargherita.configure(state = DISABLED)
        E_Margherita.set("0")

def chk_Deluxe_Veggie():
    if(var12.get() == 1):
        txtDeluxe_Veggie.configure(state = NORMAL)
        txtDeluxe_Veggie.delete('0',END)
        txtDeluxe_Veggie.focus()
    elif(var12.get() == 0):
        txtDeluxe_Veggie.configure(state = DISABLED)
        E_Deluxe_Veggie.set("0")

def chk_Veg_Extravaganza():
    if(var13.get() == 1):
        txtVeg_Extravaganza.configure(state = NORMAL)
        txtVeg_Extravaganza.delete('0',END)
        txtVeg_Extravaganza.focus()
    elif(var13.get() == 0):
        txtVeg_Extravaganza.configure(state = DISABLED)
        E_Veg_Extravaganza.set("0")

def chk_Peppy_Paneer():
    if(var14.get() == 1):
        txtPeppy_Paneer.configure(state = NORMAL)
        txtPeppy_Paneer.delete('0',END)
        txtPeppy_Paneer.focus()
    elif(var14.get() == 0):
        txtPeppy_Paneer.configure(state = DISABLED)
        E_Peppy_Paneer.set("0")

def chk_Indi_Tandoori_paneer():
    if(var15.get() == 1):
        txtIndi_Tandoori_paneer.configure(state = NORMAL)
        txtIndi_Tandoori_paneer.delete('0',END)
        txtIndi_Tandoori_paneer.focus()
    elif(var15.get() == 0):
        txtIndi_Tandoori_paneer.configure(state = DISABLED)
        E_Indi_Tandoori_paneer.set("0")

def chk_Mexican_Green_Wave():
    if(var16.get() == 1):
        txtMexican_Green_Wave.configure(state = NORMAL)
        txtMexican_Green_Wave.delete('0',END)
        txtMexican_Green_Wave.focus()
    elif(var16.get() == 0):
        txtMexican_Green_Wave.configure(state = DISABLED)
        E_Mexican_Green_Wave.set("0")

def clean_money(value):
    try:
        # Parse string as Python literal (e.g., tuple)
        parsed = ast.literal_eval(value)
        if isinstance(parsed, tuple) and len(parsed) == 2:
            return f"{parsed[0]} {parsed[1]}"
        else:
            return value
    except:
        return value

def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + '\t' + DateofOrder.get() + '\n')
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items\n")

    # List of items and their associated StringVar variables
    items = [
        ("Sprite", E_Sprite),
        ("Pepsi", E_Pepsi),
        ("DietCoke", E_DietCoke),
        ("Mojito", E_Mojito),
        ("Cappuccino", E_Cappuccino),
        ("Fanta", E_Fanta),
        ("CocaCola", E_CocaCola),
        ("ColdCoffee", E_ColdCoffee),
        ("Cheese N Corn", E_Cheese_N_Corn),
        ("Peri Peri Veg", E_African_peri_peri_veg),
        ("Margherita", E_Margherita),
        ("Deluxe Veggie", E_Deluxe_Veggie),
        ("Veg Extravaganza", E_Veg_Extravaganza),
        ("Peppy Paneer", E_Peppy_Paneer),
        ("Indi Tandoori Paneer", E_Indi_Tandoori_paneer),
        ("Mexican Green Wave", E_Mexican_Green_Wave),
    ]

    # Only print ordered items
    for item_name, item_var in items:
        value = item_var.get()
        if value.strip() != "" and value != "0":
            txtReceipt.insert(END, f'{item_name}:\t\t\t\t\t{value}\n')

    # Print totals (formatted nicely)
    txtReceipt.insert(END, 'Cost of Drinks:\t\t\t\t' + clean_money(CostofDrinks.get()) + '\n')
    txtReceipt.insert(END, 'Tax Paid:\t\t\t\t' + clean_money(PaidTax.get()) + '\n')
    txtReceipt.insert(END, 'Cost of Foods:\t\t\t\t' + clean_money(CostofFood.get()) + '\n')
    txtReceipt.insert(END, 'SubTotal:\t\t\t\t' + clean_money(SubTotal.get()) + '\n')
    txtReceipt.insert(END, 'Service Charge:\t\t\t\t' + clean_money(ServiceCharge.get()) + '\n')
    txtReceipt.insert(END, 'Total Cost:\t\t\t\t' + clean_money(TotalCost.get()) + '\n')


#Drinks#
Sprite=Checkbutton(Drinks_F,text='Sprite',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chkSprite).grid(row=0,sticky=W)
Pepsi=Checkbutton(Drinks_F,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chkPepsi).grid(row=1,sticky=W)
DietCoke=Checkbutton(Drinks_F,text='DietCoke',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chk_DietCoke).grid(row=2,sticky=W)
Mojito=Checkbutton(Drinks_F,text='Mojito',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chk_Mojito).grid(row=3,sticky=W)
Cappuccino=Checkbutton(Drinks_F,text='Cappuccino',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chk_Cappuccino).grid(row=4,sticky=W)
Fanta=Checkbutton(Drinks_F,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chk_Fanta).grid(row=5,sticky=W)
CocaCola=Checkbutton(Drinks_F,text='CocaCola',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chk_CocaCola).grid(row=6,sticky=W)
ColdCoffee=Checkbutton(Drinks_F,text='ColdCoffee',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='#ea3c53',command=chk_ColdCoffee).grid(row=7,sticky=W)

#Drink Entry#

txtSprite = Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=0,column=1)

txtPepsi = Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Pepsi)
txtPepsi.grid(row=1,column=1)

txtDietCoke = Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_DietCoke)
txtDietCoke.grid(row=2,column=1)

txtMojito= Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Mojito)
txtMojito.grid(row=3,column=1)

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Cappuccino)
txtCappuccino.grid(row=4,column=1)

txtFanta = Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Fanta)
txtFanta.grid(row=5,column=1)

txtCocaCola = Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtColdCoffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_ColdCoffee)
txtColdCoffee.grid(row=7,column=1)

#Foods#

Cheese_N_Corn = Checkbutton(Food_F,text="Cheese N Corn\t\t\t",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_Cheese_N_Corn).grid(row=0,sticky=W)
African_peri_peri_veg = Checkbutton(Food_F,text="Peri Peri Veg",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_African_peri_peri_veg).grid(row=1,sticky=W)
Margherita = Checkbutton(Food_F,text="Margherita ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_Margherita).grid(row=2,sticky=W)
Deluxe_Veggie = Checkbutton(Food_F,text="Deluxe Veggie ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_Deluxe_Veggie).grid(row=3,sticky=W)
Veg_Extravaganza = Checkbutton(Food_F,text="Veg Extravaganza ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_Veg_Extravaganza).grid(row=4,sticky=W)
Peppy_Paneer = Checkbutton(Food_F,text="Peppy Paneer ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_Peppy_Paneer).grid(row=5,sticky=W)
Indi_Tandoori_paneer = Checkbutton(Food_F,text="Indi Tandoori paneer ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_Indi_Tandoori_paneer).grid(row=6,sticky=W)
Mexican_Green_Wave = Checkbutton(Food_F,text="Mexican Green Wave ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',17,'bold'),bg='#ea3c53',command=chk_Mexican_Green_Wave).grid(row=7,sticky=W)


#Entry Foods#
txtCheese_N_Corn=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Cheese_N_Corn)
txtCheese_N_Corn.grid(row=0,column=1)

txtAfrican_peri_peri_veg=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_African_peri_peri_veg)
txtAfrican_peri_peri_veg.grid(row=1,column=1)

txtMargherita=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Margherita)
txtMargherita.grid(row=2,column=1)

txtDeluxe_Veggie=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Deluxe_Veggie)
txtDeluxe_Veggie.grid(row=3,column=1)

txtVeg_Extravaganza=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Veg_Extravaganza)
txtVeg_Extravaganza.grid(row=4,column=1)

txtPeppy_Paneer=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Peppy_Paneer)
txtPeppy_Paneer.grid(row=5,column=1)

txtIndi_Tandoori_paneer=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Indi_Tandoori_paneer)
txtIndi_Tandoori_paneer.grid(row=6,column=1)

txtMexican_Green_Wave=Entry(Food_F,font=('arial',16,'bold'),bd=4,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Mexican_Green_Wave)
txtMexican_Green_Wave.grid(row=7,column=1)


#Total Cost#
lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='cornsilk',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=4,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='cornsilk',
                fg='black',justify=RIGHT)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=4,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)



#Payment information#

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='Total',bg='cornsilk',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=3,column=0,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=4,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=3,column=1)

#RECEIPT#
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


#BUTTONS#

btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='cornsilk',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='cornsilk',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='cornsilk',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='cornsilk',command=iExit).grid(row=0,column=3)

#Display#
'''
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    '''
