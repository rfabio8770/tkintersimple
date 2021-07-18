from tkinter import Tk, Label, Entry, Button

ventana = Tk()
ventana.title("Ejemplo de Relative Place")
ventana.geometry("400x200")

def fnsuma():
    num1 = txt1.get()
    num2 = txt2.get()
    num3 = float(num1) + float(num2)
    txt3.delete(0,'end')
    txt3.insert(0, num3)

lbl1 = Label(ventana, text="Primer número:",bg="yellow")
lbl1.place(relx=0.03,rely=0.04,relwidth=0.23,relheight=0.1)
txt1 = Entry(ventana, bg="pink")
txt1.place(relx=0.3, rely=0.04, relwidth=0.22, relheight=0.1)

lbl2 = Label(ventana, text="Segundo número:",bg="yellow")
lbl2.place(relx=0.03,rely=0.17,relwidth=0.23,relheight=0.1)
txt2 = Entry(ventana, bg="pink")
txt2.place(relx=0.3, rely=0.17, relwidth=0.22, relheight=0.1)

btn = Button(ventana, text="Sumar",command=fnsuma)
btn.place(relx=0.55, rely=0.17,relwidth=0.20, relheight=0.1)

lbl3 = Label(ventana, text="Resultado:",bg="yellow")
lbl3.place(relx=0.03,rely=0.35,relwidth=0.23,relheight=0.1)
txt3 = Entry(ventana, bg="pink")
txt3.place(relx=0.3, rely=0.35, relwidth=0.22, relheight=0.1)

ventana.mainloop()
