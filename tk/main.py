from tkinter import Tk, Label, Button, Entry, PhotoImage

vent = Tk()
vent.title("Problema Cero")
vent.geometry("1000x800")

imagen = PhotoImage(file = "3f6bae5cefac261b1b131fe3cb2d867a.gif")
lbl_img = Label(vent, image= imagen)
lbl_img.pack() 
lbl_img.place(x = 0, y = 0, relwidth = 1, relheight = 1)

def fnSuma():
    Qgente= txt1.get()
    time1 = txtt.get()
    personas= txtp.get()
    Qg= float(Qgente) * float(time1)*float(personas)*1055
    Qaparatos= txt2.get()
    time2 = txtt2.get()
    QaparatosT= float(Qaparatos) * float(time2) * 3600
    Qtotal = float(Qg) + float(QaparatosT)
    txt3.insert(0,Qtotal)

lbl1 = Label(vent, text= "Qgente", bg = "yellow")
lbl1.place(x = 10, y = 10, width = 100, height = 30)

lblp = Label(vent, text= "Cantidad de personas", bg = "yellow")
lblp.place(x = 210, y = 10, width = 150, height = 30)

txt1 = Entry(vent,  bg = "pink")
txt1.place(x = 120, y = 10, width = 100, height = 30)

txtp = Entry(vent,  bg = "pink")
txtp.place(x = 350, y = 10, width = 100, height = 30)

lblt = Label(vent, text= "Cantidad de tiempo", bg = "yellow")
lblt.place(x = 420, y = 10, width = 150, height = 30)

txtt = Entry(vent,  bg = "pink")
txtt.place(x = 570, y = 10, width = 100, height = 30)

lbl2 = Label(vent, text= "Qaparatos", bg = "yellow")
lbl2.place(x = 10, y = 50, width = 100, height = 30)

btn1 = Button(vent, text = "Sumar", command=fnSuma)
btn1.place(x = 450, y = 50, width = 80, height = 30)

lblt2 = Label(vent, text= "Cantidad de tiempo", bg = "yellow")
lblt2.place(x = 230, y = 50, width = 150, height = 30)

txt2 = Entry(vent,  bg = "pink")
txt2.place(x = 120, y = 50, width = 100, height = 30)


txtt2 = Entry(vent,  bg = "pink")
txtt2.place(x = 350, y = 50, width = 100, height = 30)

lbl3 = Label(vent, text= "Qtotal", bg = "yellow")
lbl3.place(x = 10, y = 90, width = 100, height = 30)

txt3 = Entry(vent,  bg = "pink")
txt3.place(x = 120, y = 90, width = 100, height = 30)

def fnMultiplica():
    Closa1 = txt4.get()
    Closa2 = txt5.get()
    Closa3 = txt6.get()
    Ctotal = 2300 * float(Closa1) * float(Closa2) * float(Closa3) * 653
    txt7.insert(0,Ctotal)

lbl4 = Label(vent, text= "Concreto Fondo de la habitacion", bg = "yellow")
lbl4.place(x = 10, y = 130, width = 150, height = 30)

txt4 = Entry(vent,  bg = "pink")
txt4.place(x = 120, y = 130, width = 100, height = 30)

lbl5 = Label(vent, text= "Concreto Frente de la habitacion", bg = "yellow")
lbl5.place(x = 10, y = 170, width = 150, height = 30)

txt5 = Entry(vent,  bg = "pink")
txt5.place(x = 120, y = 170, width = 100, height = 30)

btn2 = Button(vent, text = "multiplicar", command=fnMultiplica)
btn2.place(x = 230, y = 170, width = 80, height = 30)

lbl6 = Label(vent, text= "El Grueso del concreto", bg = "yellow")
lbl6.place(x = 10, y = 210, width = 130, height = 30)

txt6 = Entry(vent,  bg = "pink")
txt6.place(x = 120, y = 210, width = 100, height = 30)


lbl7 = Label(vent, text= "Mlosa Closa Total", bg = "yellow")
lbl7.place(x = 10, y = 250, width = 130, height = 30)

txt7 = Entry(vent,  bg = "pink")
txt7.place(x = 120, y = 250, width = 100, height = 30)

def fndivision():
    Qtotal = txt3.get()
    Ctotal = txt7.get()
    Tfinal = float(Qtotal) / float(Ctotal)
    txt8.insert(0,Tfinal)
    


lbl8 = Label(vent, text= "Aumento de temperatura", bg = "yellow")
lbl8.place(x = 10, y = 290, width = 130, height = 30)

txt8 = Entry(vent,  bg = "pink")
txt8.place(x = 120, y = 290, width = 100, height = 30)

btn3 = Button(vent, text = "temp aumenta", command=fndivision)
btn3.place(x = 230, y = 290, width = 80, height = 30)


def fndelta():
    Tinicial = txt9.get()
    Tfinal = txt8.get()
    Tover = float(Tinicial) + float(Tfinal)
    txt10.insert(0,Tover)
lbl9 = Label(vent, text= "Temp inicial", bg = "yellow")
lbl9.place(x = 10, y = 330, width = 130, height = 30)

txt9 = Entry(vent,  bg = "pink")
txt9.place(x = 120, y = 330, width = 100, height = 30)

lbl10 = Label(vent, text= "Temp final", bg = "yellow")
lbl10.place(x = 10, y = 370, width = 130, height = 30)

txt10 = Entry(vent,  bg = "pink")
txt10.place(x = 120, y = 370, width = 100, height = 30)

btn4 = Button(vent, text = "temp fimal", command=fndelta)
btn4.place(x = 230, y = 370, width = 80, height = 30)

vent.mainloop()

