import tkinter as tk  # Importe le module tkinter
import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect('equation.db')
        self.cursor = self.con.cursor()
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS equations (date TEXT, equations TEXT)''')

    def insertInto(self, date, equation):

        self.cursor.execute("INSERT INTO equations (?, ?)", (date,  equation))


class Application(tk.Frame):  # objet
    def __init__(self, master):  #
        Database()

        super().__init__(master)
        self.grid()
        self.master = master

        self.master.geometry("350x150")

        self.Title = tk.Label(self.master, text="Bienvenue dans imprimeFonction", anchor="w")
        self.Title.grid(padx=0, pady=0)

        self.eqTxt = tk.Label(self.master, text="Equations :", anchor="w")
        self.eqTxt.grid(padx=85, pady=10)

        self.entryEq = tk.Entry(self.master)
        self.entryEq.grid(padx=85, pady=0)

        self.confirmBtn = tk.Button(self.master, text="Valider")
        self.confirmBtn.grid(padx=0, pady=5)

        print(self.entryEq.get())


root = tk.Tk()
myApp = Application(root)
myApp.mainloop()
