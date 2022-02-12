import tkinter as tk  # Importe le module tkinter
import sqlite3 # Importe le module sqlite 3 qui servira à créer une base de données et la géré.
from datetime import datetime
import sys
import numpy as np

limit_PLUSx = 50
limit_MOINSx = -50
limit_PLUSy = 10
limit_MOINSy = -10

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    elif n == 1:
        return([start])
    else:
        return([])

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
        self.AValue = str(self.EntryAString.get())
        self.BValue = str(self.EntryBString.get())
        self.CValue = str(self.EntryCString.get())
        print(self.AValue + "****" + self.BValue + "****" + self.CValue)
        for numb in numbers:
            print(numb)
            if self.CValue.startswith(numb) and self.BValue.startswith(numb) and self.AValue.startswith(numb):
                self.AValueInt = int(self.AValue)
                self.BValueInt = int(self.BValue)
                self.CValueInt = int(self.CValue)
                print(str(self.AValueInt) + " " + str(self.BValueInt) + " " + str(self.CValueInt))



    def delta(self):
        self.a = int(self.EntryEqA.get())
        self.b = int(self.EntryEqB.get())
        self.c = int(self.EntryEqC.get())
        self.deltaval = (self.b * self.b) - (4 * self.a * self.c)
        print("Delta : " + str(self.deltaval))
        self.x = -(self.b/(2*self.a))
        self.y = ((4*self.a*self.c) - (self.b*self.b))/(4*self.a)
        self.sommet = [self.x, self.y]
        print("Coordonées du sommet")
        print(self.sommet)
        self.calculateAllPoint()

    def calculateAllPoint(self):
        self.xy = []
        for x in seq(-3, 3, 0.01):
            self.xcarre = round(x, 2)*round(x, 2)
            print(self.xcarre)
            self.ax = self.a * self.xcarre
            self.bx = self.b * round(x, 2)
            self.result = self.ax + self.bx + self.c
            self.xy.append([round(x, 2), self.result])

        print(self.xy)
        self.writeOnGcodeFile()

    def writeOnGcodeFile(self):
        self.filegcode = "function.gcode"
        with open(self.filegcode, "w") as f:
            for x, y in self.xy:
                if not x+4 > limit_PLUSx and not x < limit_MOINSx:
                    if not y > limit_PLUSy and not y < limit_MOINSy:
                        f.write(f'G1 X{x+4} Y{y} ;\n')

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

        self.EntryAString = tk.StringVar(self)
        self.EntryEqA = tk.Entry(self.master, text="La valeur de a", textvariable=self.EntryAString, width=25)
        self.EntryEqA.insert(0, 'Entrée la valeur de a (ax²)')
        self.EntryEqA.grid(padx=75, pady=0)
        self.EntryEqA.bind("<Button-1>", lambda a = "a": self.click("a"))

        self.EntryBString = tk.StringVar(self)
        self.EntryEqB = tk.Entry(self.master, text="La valeur de b", textvariable=self.EntryBString, width=25)
        self.EntryEqB.insert(0, 'Entrée la valeur de b (bx)')
        self.EntryEqB.grid(padx=75, pady=1)
        self.EntryEqB.bind("<Button-1>", lambda b = "b" : self.click("b"))

        self.EntryCString = tk.StringVar(self)
        self.EntryEqC = tk.Entry(self.master, text="La valeur de c", textvariable= self.EntryCString , width=25)
        self.EntryEqC.insert(0, 'Entrée la valeur de c (c)')
        self.EntryEqC.grid(padx=75, pady=1)
        self.EntryEqC.bind("<Button-1>", lambda c = "c": self.click("c"))

        self.confirmBtn = tk.Button(self.master, text="Valider", command = self.getText )
        self.confirmBtn.grid(padx=0, pady=5)


if __name__ == '__main__':
    root = tk.Tk()
    myApp = Application(root)
    myApp.mainloop()
