from tkinter import Tk, Label, Entry, Button, Frame

class FrmPrincipal(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=320,height=170)
        self.master = master
        self.pack()
        self.crearWidgets()

    def fnsuma(self):
        num1 = self.txt1.get()
        num2 = self.txt2.get()
        num3 = float(num1) + float(num2)
        self.txt3.delete(0,'end')
        self.txt3.insert(0, num3)

    def crearWidgets(self):
        self.lbl1 = Label(self, text="Primer número:",bg="yellow")
        self.txt1 = Entry(self, bg="pink")
        self.lbl2 = Label(self, text="Segundo número:",bg="yellow")
        self.txt2 = Entry(self, bg="pink")
        self.btn = Button(self, text="Sumar",command=self.fnsuma)
        self.lbl3 = Label(self, text="Resultado:",bg="yellow")
        self.txt3 = Entry(self, bg="pink")
     
        self.lbl1.place(x=10,y=10,width=100, height=30)
        self.txt1.place(x=120,y=10,width=100, height=30)
        self.lbl2.place(x=10,y=50,width=100, height=30)
        self.txt2.place(x=120,y=50,width=100, height=30)
        self.btn.place(x=230,y=50,width=80, height=30)
        self.lbl3.place(x=10,y=120,width=100, height=30)
        self.txt3.place(x=120,y=120,width=100, height=30)

root = Tk()
root.wm_title("Suma de dos números")
app = FrmPrincipal(root)
app.mainloop()
