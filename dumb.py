from tkinter import *
from random import randint

class Application:
    def __init__(self, master=None):
        self.defaultFont = ("Arial", "10")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 25
        self.secondContainer["pady"] = 75
        self.secondContainer.pack(side=LEFT)

        self.titulo = Label(self.firstContainer, text="Você é burro?")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()

        self.btnYes = Button(self.secondContainer)
        self.btnYes["text"] = "SIM"
        self.btnYes["font"] = ("Calibri", "10")
        self.btnYes["bg"] = '#333'
        self.btnYes["fg"] = '#fff'
        self.btnYes["width"] = 10
        self.btnYes["height"] = 3
        self.btnYes["command"] = self.changeTxt
        self.btnYes.pack()

        self.btnNot = Button(master)
        self.btnNot["text"] = "NÃO"
        self.btnNot["font"] = ("Calibri", "10")
        self.btnNot["width"] = 10
        self.btnNot["height"] = 3
        self.btnNot["bg"] = '#333'
        self.btnNot["fg"] = '#fff'
        self.btnNot["command"] = self.changePos
        self.btnNot.place(x=313, y=183, anchor=CENTER)

    def changePos(self):
        self.btnNot.place(x=randint(180, 330), y=randint(100, 220), anchor=CENTER)

    def changeTxt(self):
        self.btnNot["command"] = False
        self.titulo["text"] = "EU SEMPRE SOUBE!!!"
        root.after(900, root.destroy)

root = Tk()
root.title('Aplicação sem respeito')
root.geometry('380x300')
root.resizable(width=False, height=False)
Application(root)
root.mainloop()