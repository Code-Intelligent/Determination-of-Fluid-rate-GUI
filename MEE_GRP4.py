import tkinter as tk
from tkinter import ttk
from math import pi,sqrt

root = tk.Tk()
root.title('Welcome to MEE 307 Student Project By GROUP 4')
root.geometry('1600x800')

def get_value():
    P1 = float(a.get())
    P2 = float(b.get())
    D1 = float(e.get())
    D2 = float(f.get())
    density = float(i.get())
    g = float(j.get())
   
    A1 = (pi*(D1**2))/4 #Area 1

    A2 = (pi*(D2**2))/4 #Area 2

    k = A1/A2  # k is area ratio

    PH1 = P1/(density*g) # pressure head 1

    PH2 = -5.44   # pressure 

    PH_diff = PH1 - PH2 # pressure head difference

    PH_loss = 0.03*PH_diff #pressure head loss

    cd = ((PH_diff - PH_loss)/(PH_diff))**0.5  

    nume = 2*g*PH_diff   # numerator

    deno = ((k**2)-1)  # denominaor
    
    square_root = (nume/deno)**0.5  #square root
    Q = (cd*A1*square_root)*100   #Flow rate

    Area1.set(str(A1))
    Area2.set(str(A2))
    Area_ratio.set(str(k))
    Pressure_head_1.set(str(PH1))
    Pressure_head_2.set(str(PH2))
    Pressure_head_diff.set(str(PH_diff))
    Pressure_head_loss.set(str(PH_loss))
    Discharge_coff.set(str(cd))
    Flow_rate.set(str(Q))


Area1=tk.StringVar()    
Area2=tk.StringVar()
Area_ratio=tk.StringVar()
Pressure_head_1=tk.StringVar()
Pressure_head_2=tk.StringVar()
Pressure_head_diff=tk.StringVar()
Pressure_head_loss=tk.StringVar()
Discharge_coff=tk.StringVar()
Flow_rate=tk.StringVar()

       
a = tk.StringVar()#
b = tk.StringVar()#
e = tk.StringVar()#
f = tk.StringVar()#
i = tk.StringVar()#
j = tk.StringVar()#

#------------------------------------------The heading-------------------------------------------------------
lbl = tk.Label(root,text='DETERMINATION OF FLUID FLOW RATE',bg='powder blue',font=('arial',12,'bold'),bd=5)
lbl.pack(side='top')

#------------------------------------------------------------------------------------------------------------
btn = tk.Button(root,text='SOLVE',width=15,font=('arial',10,'bold'),command=get_value,bg='red',bd=5)
btn.place(x=600,y=300)

lbl = tk.Label(root,text='INPUT',font=('arial',15,'bold'),bd=20,bg='powder blue',fg='green')
lbl.place(x=0,y=20)
# --------------------------P1 is pressure1-------------------------------------------------------------

lbl = tk.Label(root,text='Pressure 1',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=0,y=80)
p1 = tk.Entry(root,textvariable=a,width=20,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
p1.place(x=160,y=80)
lbl = tk.Label(root,text='N/m²',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=370,y=80)

# -------------P2 is pressure2------------------------------------------------------------------------------- 
lbl = tk.Label(root,text='Pressure 2',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=0,y=160)
p2 = tk.Entry(root,width=20,textvariable=b,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
p2.place(x=160,y=160)
lbl = tk.Label(root,text='N/m²',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=370,y=160)

# -------------d1 is Diameter1-------------------------------------------------------------------------------------- 
lbl = tk.Label(root,text='Diameter 1',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=0,y=240)

d1 = tk.Entry(root,width=20,textvariable=e,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
d1.place(x=160,y=240)

lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=370,y=240)

# -------------d2 is diameter 2 --------------------- 
lbl = tk.Label(root,text='Diameter 2',font=('arial',12,'bold'),bg='powder blue',bd=5,fg='green')
lbl.place(x=0,y=320)
d2 = tk.Entry(root,width=20,textvariable=f,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
d2.place(x=160,y=320)
lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=370,y=320)


# -------------gra is gravity--------------------- 
lbl = tk.Label(root,text='Gravity',font=('arial',12,'bold'),bg='powder blue',bd=5,fg='green')
lbl.place(x=0,y=400)
gra = tk.Entry(root,width=20,textvariable=i,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
gra.place(x=160,y=400)
lbl = tk.Label(root,text='m/s²',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=370,y=400)

# -------------D is Density--------------------- 
lbl = tk.Label(root,text='Density',font=('arial',12,'bold'),bd=5,fg='green',bg='powder blue',)
lbl.place(x=0,y=480)
D = tk.Entry(root,textvariable=j,width=20,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
D.place(x=160,y=480)
lbl = tk.Label(root,text='kg/m³',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='green')
lbl.place(x=370,y=480)

#-----------------------Right handside--------------------------------------------------

lbl = tk.Label(root,text='OUTPUT',font=('arial',15,'bold'),bd=20,bg='powder blue',fg='blue')
lbl.place(x=1020,y=20)
# -------------Ph1 is pressure head 1-------------------------------------------------------------------------- 
lbl = tk.Label(root,text='Pressure head 1',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=80)
ph1 = tk.Entry(root,width=20,text=Pressure_head_1,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
ph1.place(x=1020,y=80)
lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,fg='blue',bg='powder blue',)
lbl.place(x=1230,y=80)

# -------------ph2 is pressure 2--------------------------------------------------------------------------------- 
lbl = tk.Label(root,text='Pressure head 2',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=140)
ph2 = tk.Entry(root,width=20,text=Pressure_head_2,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
ph2.place(x=1020,y=140)
lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=1230,y=140)

# -------------ph is pressure head----------------------------------------------------------------------------------------- 
lbl = tk.Label(root,text='Pressure head diff.',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=200)
ph = tk.Entry(root,width=20,text=Pressure_head_diff,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
ph.place(x=1020,y=200)
lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=1230,y=200)

# ---------------------------------------------------a1 is area1----------------------------------------------- 
lbl = tk.Label(root,text='Area 1',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=260)
a1 = tk.Entry(root,width=20,text=Area1,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
a1.place(x=1020,y=260)
lbl = tk.Label(root,text='m²',font=('arial',12,'bold'),bd=5,fg='blue',bg='powder blue',)
lbl.place(x=1230,y=260)

# ---------------------------------------------------a2 is area2----------------------------------------------------- 
lbl = tk.Label(root,text='Area 2',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=320)
a2 = tk.Entry(root,width=20,text=Area2,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
a2.place(x=1020,y=320)
lbl = tk.Label(root,text='m²',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=1230,y=320)

# -------------K is area ratio--------------------- 
lbl = tk.Label(root,text='K',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=380)
K = tk.Entry(root,width=20,text=Area_ratio,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
K.place(x=1020,y=380)

# -------------pl is pressure head loss--------------------- 
lbl = tk.Label(root,text='pressure head loss',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=440)
pl = tk.Entry(root,width=20,text=Pressure_head_loss,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
pl.place(x=1020,y=440)
lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=1230,y=440)

# -------------DC is discharge coff.--------------------- 
lbl = tk.Label(root,text='Discharge coefficient',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='blue')
lbl.place(x=850,y=500)
DC = tk.Entry(root,width=20,text=Discharge_coff,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
DC.place(x=1020,y=500)

#-------------F_R is flow rate--------------------- 
lbl = tk.Label(root,text='Flow rate',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='indigo')
lbl.place(x=420,y=600)
F_R = tk.Entry(root,width=25,text=Flow_rate,font=('arial',12,'bold'),bd=5,fg='black',insertwidth=5)
F_R.place(x=530,y=600)
lbl = tk.Label(root,text='litre/s',font=('arial',12,'bold'),bd=5,bg='powder blue',fg='indigo')
lbl.place(x=770,y=600)

root.configure(background='powder blue')
root.mainloop()

