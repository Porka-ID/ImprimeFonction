import tkinter as tk  # Importe le module tkinter
import sqlite3 # Importe le module sqlite 3 qui servira à créer une base de données et la géré.
from datetime import datetime
import sys

class Database():
    def __init__(self):
        self.con = sqlite3.connect('equation.db')
        self.cursor = self.con.cursor()
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS equations (date TEXT, equations TEXT)''')

    def insertInto(self, date, equation):

        self.cursor.execute("INSERT INTO equations (?, ?)", (date,  equation))


class Application(tk.Frame):  # objet
    def click(self, *args):
        self.EntryEqA.delete(0, 'end')

    def leave(self):
        self.destroy()
        exit()

    def __init__(self, master):  #
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
        self.EntryEqA.bind("<Button-1>", self.click)

        self.EntryEqB = tk.Entry(self.master, text="La valeur de b", width=25)
        self.EntryEqB.insert(0, 'Entrée la valeur de b (bx)')
        self.EntryEqB.grid(padx=75, pady=1)
        self.EntryEqB.bind("<Button-1>", self.click)

        self.EntryEqC = tk.Entry(self.master, text="La valeur de c", width=25)
        self.EntryEqC.insert(0, 'Entrée la valeur de c (c)')
        self.EntryEqC.grid(padx=75, pady=1)
        self.EntryEqC.bind("<Button-1>", self.click)

        self.confirmBtn = tk.Button(self.master, text="Valider", command = self.leave )
        self.confirmBtn.grid(padx=0, pady=5)



root = tk.Tk()
myApp = Application(root)
myApp.mainloop()
