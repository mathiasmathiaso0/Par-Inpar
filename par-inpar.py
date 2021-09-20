from tkinter import *
from tkinter import messagebox


#Funciones
def botonAceptarFuncion():
    entrada = int(entradaDatos.get())
    if int(entrada) % 2 == 0:
        messagebox.showinfo(message=f"El numero {entrada} es par", title="Par")
    else: 
        messagebox.showinfo(message=f"El numero {entrada} es inpar", title="Inpar")

root = Tk()
root.title("Par o Inpar")
root.geometry("300x50")

textFirst = Label(root, text= "Ingrese un numero")
textFirst.grid(row=4, column=2)
textFirst.config(pady= "10px")
 
entradaDatos = Entry(root)
entradaDatos.grid(row=4, column=3)

botonAceptar1 = Button(root, text="Aceptar", command= lambda: botonAceptarFuncion())
botonAceptar1.grid(row= 4, column= 4)
botonAceptar1.place(x="180px", y="7px")

root.mainloop()
