from tkinter import Tk, Button, Entry

# Configuración ventana principal
#ejecucion del teclado virtual
def tecladonumerico(d):
    i=pantalla.get()
    k=len(i)
    pantalla.insert(k+1,d)
#ejecucion de igual
def operacion():
    try:
        i=pantalla.get()
        p=""
        g=""
        s=""
        t=False
        for d in i:
            if d=="+" or d=="-" or d=="*" or d=="/":
                t=True
                s=d
            elif t==False:
                p+=d
            else:
                g+=d
        p=float(p)
        g=float(g)
        pantalla.delete(0, "end")
        if s=="+":
            pantalla.insert(0,p+g)
        elif s=="-":
            pantalla.insert(0,p-g)
        elif s=="*":
            pantalla.insert(0,p*g)
        else:
            pantalla.insert(0,p/g)
    except:
        pantalla.delete(0, "end")
            
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x270")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=50, padx=1, pady=1,sticky="nw")

# Configuración botones
boton_1 = Button(root, text="1",command=lambda: tecladonumerico("1"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=0, pady=0,sticky="nw")
boton_2 = Button(root, text="2",command=lambda: tecladonumerico("2"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=0, pady=0,sticky="nw")
boton_3 = Button(root, text="3",command=lambda: tecladonumerico("3"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=0, pady=0,sticky="nw")
boton_4 = Button(root, text="4",command=lambda: tecladonumerico("4"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1,sticky="nw")
boton_5 = Button(root, text="5",command=lambda: tecladonumerico("5"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1,sticky="nw")
boton_6 = Button(root, text="6",command=lambda: tecladonumerico("6"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1,sticky="nw")
boton_7 = Button(root, text="7",command=lambda: tecladonumerico("7"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1,sticky="nw")
boton_8 = Button(root, text="8",command=lambda: tecladonumerico("8"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1,sticky="nw")
boton_9 = Button(root, text="9",command=lambda: tecladonumerico("9"), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1,sticky="nw")
boton_igual = Button(root, text="=",command=lambda: operacion(), width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1,sticky="nw")
boton_punto = Button(root, text=".",command=lambda: tecladonumerico("."), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1,sticky="nw")
boton_mas = Button(root, text="+",command=lambda: tecladonumerico("+"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=0, pady=1,sticky="nw")
boton_menos = Button(root, text="-",command=lambda: tecladonumerico("-"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=0, pady=1,sticky="nw")
boton_multiplicacion = Button(root, text="*",command=lambda: tecladonumerico("*"),  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=0, pady=1,sticky="nw")
boton_division = Button(root, text="/",command=lambda: tecladonumerico("/"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=0, pady=1,sticky="nw")

root.mainloop()
