
from tkinter import *
import time

root =Tk()
root.geometry("950x780")
root.title("     Banking App    ")
root.config(bg='black' ) 
root.resizable(0,0)
Top=Frame(root,bg='white', width= 800, height=50, relief=SUNKEN)
Top.pack(side=TOP)

global label3 
global label4 
global label5 
global lbl4 

F1=Frame(root,bg='black', width= 300, height=700, relief=SUNKEN)
F1.pack(side=LEFT)

F2=Frame(root,bg='black', width= 400, height=700, relief=SUNKEN)
F2.pack(side=RIGHT)

localtime= time.asctime(time.localtime(time.time()))

lbl1 = Label(Top,font=('aria',30,'bold') ,text = "BANKING APP",fg="powder blue",bg='black',bd=10,anchor='w')
lbl1.grid(row=0,column=0)

lbl2 = Label(Top,font=('aria',30,'bold') , text = localtime,fg="powder blue",bg='black',bd=10,anchor='w')
lbl2.grid(row=1,column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
Acca = "    "

def bank():
    global Acca
    accno = ["0009857","0107833","0007836","82498223","53285822","83258214","92851915","31414135","12415284","96388522"]
    account = number.get()
    if account in accno:
        lbl4.config(text="Reigstered User")
        bank = {"0009857" : 51215,"0107833": 14215,"0007836": 41153,"82498223":72431,"53285822":98282,"83258214":128462,"92851915":62828,"31414135":65394,"12415284":84285,"96388522":43952} # dictionary
        balance = bank[account]
        Acca = balance

    else:
        lbl4.config(text = ("Not Registered User"))

# def deposit():
#     global Acca
#     global bal
#     global amo
#     amo = float(amount.get())
#     bal = Acca + amo
#     label3.config(text = ("Net Balance : ", float(bal)))
#     return bal

def deposit():
    global Acca
    global bal
    global amo
    amo = (amount.get())
    if amo == "":
            label3.config(text = ("ENTER AMOUNT TO DEPOSIT"))
    else:
        amo = float(amount.get())
        bal = Acca + amo
        label3.config(text = ("Net Balance : ", float(bal)))
    return bal

current_bal = " "
bal = current_bal

def withdrawn():
    global Acca
    global ace
    wd = float(withd.get())   
    if Acca >= wd:
        ace = bal - wd 
        label4.config(text = ("Net Balance : ", float(ace)))
    else:
        label4.config(text="Insufficient Balance")

def bal():
    global Acca
    label5.config(text = ("Net Balance", float(ace)))

def fd():
    root=Tk()
    root.title("Fixed Deposit Section")
    root.geometry('1100x900')
    root.config(bg='#37306B')
    root.resizable(0,0)

    namelbl = Label(root,text = "NAME",font=('aria' ,15),fg='#3C2A21')
    namelbl.place(x=50,y=50)
    ballbl = Label(root,text = "BALANCE",font=('aria' ,15),fg='#3C2A21')
    ballbl.place(x=180,y=50)
    matlbl= Label(root,text = "MATURITY AMOUNT",font=('aria' ,15),fg='#3C2A21')
    matlbl.place(x=350,y=50)
    matdalbl = Label(root,text = "MATURITY DATE",font=('aria' ,15),fg='#3C2A21')
    matdalbl.place(x=580,y=50)
    ratlbl = Label(root,text = "INTEREST RATE",font=('aria' ,15),fg='#3C2A21')
    ratlbl.place(x=800,y=50)

    name1=Label(root, text = "SUMEDH",font=('aria' ,15),fg='#B3005E')
    name1.place(x=50,y=140)
    bal1=Label(root,text="58,87,543",font=('aria' ,15),fg='#B3005E')
    bal1.place(x=180,y=140)
    mat_amo =Label(root,text= "1,28,94,513",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=140)
    mat_date = Label(root,text= "09/08/2039",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=140)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=140)

    name2=Label(root, text = "DEVESH",font=('aria' ,15),fg='#B3005E')
    name2.place(x=50,y=210)
    bal2=Label(root,text="8,42,533",font=('aria' ,15),fg='#B3005E')
    bal2.place(x=180,y=210)
    mat_amo =Label(root,text= "21,51,461",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=210)
    mat_date = Label(root,text= "09/08/2029",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=210)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=200)

    name3=Label(root, text = "RAHUL",font=('aria' ,15),fg='#B3005E')
    name3.place(x=50,y=280)
    bal3=Label(root,text="1,22,993",font=('aria' ,15),fg='#B3005E')
    bal3.place(x=180,y=280)
    mat_amo =Label(root,text= "5,03,161",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=280)
    mat_date = Label(root,text= "02/06/2025",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=280)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=260)

    name4=Label(root, text = "LALIT",font=('aria' ,15),fg='#B3005E')
    name4.place(x=50,y=350)
    bal45=Label(root,text="5,92,093",font=('aria' ,15),fg='#B3005E')
    bal45.place(x=180,y=350)
    mat_amo =Label(root,text= "12,31,661",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=350)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=340)
    mat_date = Label(root,text= "21/02/2029",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=350)

    name5=Label(root, text = "RAJKUMAR",font=('aria' ,15),fg='#B3005E')
    name5.place(x=50,y=420)
    bal4=Label(root,text="68,503",font=('aria' ,15),fg='#B3005E')
    bal4.place(x=180,y=420)
    mat_amo =Label(root,text= "2,83,135",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=420)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=400)
    mat_date = Label(root,text= "09/09/2023",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=420)

    name6=Label(root, text = "PUSHKRAJ",font=('aria' ,15),fg='#B3005E')
    name6.place(x=50,y=490)
    bal5=Label(root,text="9,42,503",font=('aria' ,15),fg='#B3005E')
    bal5.place(x=180,y=490)
    mat_amo =Label(root,text= "18,51,416",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=490)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=460)
    mat_date = Label(root,text= "24/09/2033",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=490)

    name7=Label(root, text = "VINAY",font=('aria' ,15),fg='#B3005E')
    name7.place(x=50,y=560)
    bal6=Label(root,text="12,933",font=('aria' ,15),fg='#B3005E')
    bal6.place(x=180,y=560)
    mat_amo =Label(root,text= "1,84,455",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=560)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=530)
    mat_date = Label(root,text= "27/11/2052",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=560)

    name8=Label(root, text = "YASH",font=('aria' ,15),fg='#B3005E')
    name8.place(x=50,y=630)
    bal7=Label(root,text="3,52,523",font=('aria' ,15),fg='#B3005E')
    bal7.place(x=180,y=630)
    mat_amo =Label(root,text= "7,346,347",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=630)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=610)
    mat_date = Label(root,text= "14/03/2027",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=630)

    name9=Label(root, text = "JITESH",font=('aria' ,15),fg='#B3005E')
    name9.place(x=50,y=700)
    bal8=Label(root,text="10,22,913",font=('aria' ,15),fg='#B3005E')
    bal8.place(x=180,y=700)
    mat_amo =Label(root,text= "25,03,164",font=('aria' ,15),fg="#B3005E")
    mat_amo.place(x=350,y=700)
    int_rate=Label(root,text= "6.5",font=('aria' ,15),fg="#B3005E")
    int_rate.place(x=800,y=700)
    mat_date = Label(root,text= "05/05/2030",font=('aria' ,15),fg="#B3005E")
    mat_date.place(x=580,y=700)

    root.mainloop()


def reset():
    number.set("")
    amount.set("")
    withd.set("")

    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
    lbl4.config(text="")

def interest():
    root = Tk()
    root.title('Interest Calcuation System')
    root.geometry('500x400')
    root.config(bg='powderblue')
    
    def calculate():
        total=int(princiEntry.get())
        rat=int(rateEntry.get())
        tim=int(timeEntry.get())
        amount = (total * rat * tim)/100
        EI=Label(root,text=f"{amount}",font=('arial', 16,'bold'))
        EI.place(x=230,y=230)

    principal=Label(root,text='Principal : ',font=('times new roman',18,'bold'),bg='pink')
    principal.place(x=50,y=40)

    rate=Label(root,text='Rate Of Interest : ',font=('times new roman',18,'bold'),bg='pink')
    rate.place(x=50,y=90)

    time=Label(root,text='Time : ',font=('times new roman',18,'bold'),bg='pink')
    time.place(x=50,y=160)

    interest = Label(root, text = 'Interest Earned : ', font=('times new roman',18,'bold'),bg='pink')
    interest.place(x=50,y=230)

    principalvalue=StringVar()
    ratevalue=StringVar()
    timevalue=StringVar()

    princiEntry= Entry(root,textvariable=principalvalue,font=('arial', 20, 'bold'),width=8)
    princiEntry.place(x=200,y=30)

    rateEntry=Entry(root,textvariable=ratevalue,font=('arial', 20, 'bold'),width=5)
    rateEntry.place(x=250,y=90)

    timeEntry=Entry(root,textvariable=timevalue,font=('arial', 20, 'bold'),width=5)
    timeEntry.place(x=150,y=160)

    button = Button(root,text = 'Calculate',font =('arial' ,14),command=calculate,fg='black').place(x=350,y=40)
    exitt= Button(root,text = 'Exit',command =lambda:root.destroy(),font =('arial' ,14),width=8).place(x=350,y=90)

    root.mainloop()


lbl = Label(F1, font=('aria', 16, 'bold'), fg='#0E8388', bg='black',bd=10,text= "Enter The Account Number : ")
lbl.grid(row=0 , column=3)
text = Entry(F1 ,font=('aria', 16, 'bold'), bg='Powder Blue',bd=10,textvariable=number, insertwidth=4,justify='right')
text.grid(row=0,column=4)
lbl4 = Label(F1, font=('aria',16,'bold'),bg='black',bd=10,fg='white')
lbl4.grid(row=1,column=4)
submitbtn = Button(F2, padx= 24,pady=4,bd=10, fg='black',font=('aria',16,'bold'),width= 7 , text="SUBMIT",bg='#DFFFD8', command=bank)
submitbtn.grid(row=0,column=4)

lblTotal = Label(F1 ,text =  "                           ", fg='white', bg='black' )
lblTotal.grid(row=3, columnspan = 10)

lbl = Label(F1, font=('aria',16,'bold'),text = "Enter the amount to be Depostied : ",fg='#0E8388',bg='black',bd=10)
lbl.grid(row=4,column=3)
txt = Entry(F1, font=('aria',16,'bold'), textvariable=amount,bd=6,insertwidth=4,bg='Powder Blue', justify='right')
txt.grid(row=4,column=4)
label3=Label(F1,fg='white',bg='black',font=('aria',16,'bold'))
label3.grid(row=5,column=4)
intbutton = Button(F2, padx= 24,pady=4,bd=10, fg='black',font=('aria',16,'bold'),width= 7 , text="INTEREST",bg='#DFFFD8', command=interest)
intbutton.grid(row=4,column=4)

lblTotal = Label(F1 ,text =  "                           ", fg='white', bg='black' )
lblTotal.grid(row=7, columnspan = 10)

lbl = Label(F1, font=('aria',16,'bold'),text = "Enter the amount to be withdrawn : ",fg='#0E8388',bg='black',bd=10)
lbl.grid(row=8,column=3)
txt1 = Entry(F1, font=('aria',16,'bold'), textvariable=withd,bd=6,insertwidth=4,bg='Powder Blue', justify='right')
txt1.grid(row=8,column=4)
label4=Label(F1,fg='white',bg='black',font=('aria',16,'bold'))
label4.grid(row=9,column=4)
label5=Label(F1,fg='white',bg='black',font=('aria',16,'bold'))
label5.grid(row=10,column=4)

btndeposit = Button(F2,padx= 24,pady=4,bd=10 , fg='black', font =('aria',16,'bold'),width=7, text="DEPOSIT",bg="#DFFFD8",command=deposit)
btndeposit.grid(row=8, column=4)

btnwithdraw = Button(F2,padx= 24,pady=4,bd=10 , fg='black', font=('aria',16,'bold'),width=7, text="WITHDRAW",bg="#DFFFD8",command=withdrawn)
btnwithdraw.grid(row=10, column=4)

btnreset = Button(F2,padx= 24,pady=4,bd=10 , fg='black', font=('aria',16,'bold'),width=7, text="RESET",bg="#DFFFD8",command=reset)
btnreset.grid(row=11, column=4)

btnbal = Button(F2,padx= 24,pady=4,bd=10 , fg='black', font =('aria',16,'bold'),width=7, text="BALANCE",bg="#DFFFD8",command=bal)
btnbal.grid(row=12, column=4)

btnfd = Button(F2,padx= 24,pady=4,bd=10 , fg='black', font =('aria',16,'bold'),width=7, text="F.D",bg="#DFFFD8",command=fd)
btnfd.grid(row=13, column=4)

btnexit = Button(F2,padx= 24,pady=4,bd=10 , fg='black', font=('aria',16,'bold'),width=7, text="EXIT",bg="#DFFFD8",command= lambda:exit())
btnexit.grid(row=14, column=4)







root.mainloop()