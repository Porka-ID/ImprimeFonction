import tkinter as tk  # Importe le module tkinter
import sqlite3 # Importe le module sqlite 3 qui servira à créer une base de données et la géré.
from datetime import datetime
import sys
import math

class Database():
    def __init__(self):
        self.con = sqlite3.connect('equation.db')
        self.cursor = self.con.cursor()
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS equations (date TEXT, equations TEXT)''')

    def insertInto(self, date, equation):

        self.cursor.execute("INSERT INTO equations (?, ?)", (date,  equation))


class Application(tk.Frame):  # objet
    def click(self, result, *args):
        if result == "a":
            self.EntryEqA.delete(0, 'end')
        elif result == "b":
            self.EntryEqB.delete(0, "end")
        else:
            self.EntryEqC.delete(0, "end")

    def leave(self):
        self.destroy()
        exit()

    def getText(self):
        print(self.EntryEqA.get())
        print(self.EntryEqB.get())
        print(self.EntryEqC.get())
        self.delta()
        self.leave()

    def delta(self):
        self.a = int(self.EntryEqA.get())
        self.b = int(self.EntryEqB.get())
        self.c = int(self.EntryEqC.get())
        self.deltaval = (self.b * self.b) - (4 * self.a * self.c)
        print("Delta : " + str(self.deltaval))
        self.x = round(-(self.b/(2*self.a)), 2)
        self.y = round(((4*self.a*self.c) - (self.b*self.b))/(4*self.a), 2)
        self.sommet = [self.x, self.y]
        print("Coordonées du sommet")
        print(self.sommet)
        self.algo()

    def algo(self):
        self.list_all_value = []
        for x in range(-15, 15):
            self.acarré = (self.a*(x*x))
            self.bx = (self.b * x)
            self.c = self.c
            self.fx = self.acarré + self.bx + self.c
            self.fxdex = [x, self.fx]
            self.list_all_value.append(self.fxdex)
        print(self.list_all_value)
        self.writeGcode()

    def writeGcode(self):
        with open("myGcode.gcode", "w") as f:
            for x,y in self.list_all_value:
                f.write(f"G1 X{x} Y{y} ;\n")

    def __init__(self, master):  #
        self.a = None
        self.b = None
        self.c = None
        self.deltaval = None
        self.sommet = None
        self.x = None
        self.y = None
        Database()

        super().__init__(master)
        self.grid()
        self.master = master

        self.master.geometry("350x210")

        self.Title = tk.Label(self.master, text="Bienvenue dans imprimeFonction", anchor="w")
        self.Title.grid(padx=0, pady=0)

        self.eqTxt = tk.Label(self.master, text="Equations (ax² + bx + c) :", anchor="w")
        self.eqTxt.grid(padx=85, pady=10)

        self.EntryEqA = tk.Entry(self.master, text="La valeur de a", width=25)
        self.EntryEqA.insert(0, 'Entrée la valeur de a (ax²)')
        self.EntryEqA.grid(padx=75, pady=0)
        self.EntryEqA.bind("<Button-1>", lambda a = "a": self.click("a"))

        self.EntryEqB = tk.Entry(self.master, text="La valeur de b", width=25)
        self.EntryEqB.insert(0, 'Entrée la valeur de b (bx)')
        self.EntryEqB.grid(padx=75, pady=1)
        self.EntryEqB.bind("<Button-1>", lambda b = "b" : self.click("b"))

        self.EntryCString = tk.StringVar(self)
        self.EntryEqC = tk.Entry(self.master, text="La valeur de c", textvariable= self.EntryCString , width=25)
        self.EntryEqC.insert(0, 'Entrée la valeur de c (c)')
        self.EntryEqC.grid(padx=75, pady=1)
        self.EntryEqC.bind("<Button-1>", lambda  c = "c": self.click("c"))

        self.confirmBtn = tk.Button(self.master, text="Valider", command = self.getText )
        self.confirmBtn.grid(padx=0, pady=5)


if __name__ == '__main__':
    root = tk.Tk()
    myApp = Application(root)
    myApp.mainloop()
