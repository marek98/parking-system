import tkinter as tk
from Record import Record

class Box:
    def __init__(self, num, id, record = None,c,app):
        self.number = num
        self.idCompany = fi
        self.free = True
        self.wrong = False
        self.borrowed = False
        self.record = record
        self.button = tk.Button(c, bg = 'gray', text = 'Box '+ self.number + '\n' + 'firma', command = lambda : openBoxWin(self, app))

    def newParking(self, ECV, firm, borr):
        self.free = False
        self.borrowed = borr
        if firm != self.firm and not self.borrowed:
            self.wrong = False

    def endParking(self):
        self.free = True
        self.wrong = False
        self.borrowed = False

    def getColor(self):
        color = 'grey'
        if self.free:
            color = 'grey'
        if not self.free:
            if not borrowed:
                if not self.wrong:
                    color = 'green'
                else:
                    color = 'red'
            else:
                color = 'red'
        return color
    def changeColor(self):
        self.button.config(bg = self.getColor())

    def createRecord(self):
        #vytvor instanciu záznamu a vrat ju

    def endRecord(self):
        #zrus instanciu záznamu
