import tkinter as tk # Importe le module tkinter

class Application(tk.Frame): # objet
    def __init__(self, kk): #
        super().__init__(kk)
        self.grid()
        self.master = kk

        self.Title = tk.Label(self.master, text="Bienvenue dans imprimeFonction", anchor="w")
        self.Title.grid(column=0, row=0)

        self.eqTxt = tk.Label(self.master, text="Equations :", anchor="w")
        self.eqTxt.grid(column=0, row=1)

        self.entryEq = tk.Entry(self.master)
        self.entryEq.grid(column=0, row=2)

        print(self.entryEq.get())






root = tk.Tk()
myApp = Application(root)
myApp.mainloop()

