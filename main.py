from tkinter import Tk, Label, Entry, Button

ventana = Tk()
ventana.title("Ejemplo de Place")
ventana.geometry("400x200")

def fnsuma():
    num1 = txt1.get()
    num2 = txt2.get()
    num3 = float(num1) + float(num2)
    txt3.delete(0,'end')
    txt3.insert(0, num3)

lbl1 = Label(ventana, text="Primer número:",bg="yellow")
lbl1.place(x=10,y=10,width=100,height=30)
txt1 = Entry(ventana, bg="pink")
txt1.place(x=120, y=10, width=100, height=30)

lbl2 = Label(ventana, text="Segundo número:",bg="yellow")
lbl2.place(x=10,y=50,width=100,height=30)
txt2 = Entry(ventana, bg="pink")
txt2.place(x=120, y=50, width=100, height=30)
btn = Button(ventana, text="Sumar",command=fnsuma)
btn.place(x=230, y=50,width=80, height=20)

lbl3 = Label(ventana, text="Resultado:",bg="yellow")
lbl3.place(x=10,y=120,width=100,height=30)
txt3 = Entry(ventana, bg="pink")
txt3.place(x=120, y=120, width=100, height=30)

ventana.mainloop()