import tkinter as tk
from Record import Record
#from GUI import openBoxWin

class Box:
    def __init__(self, id, num, fiId, c, app, record = None, ztp = None):
        self.id = id
        self.number = num
        self.idCompany = fiId
        self.record = record
        self.ztp = ztp
        self.button = tk.Button(c, bg = 'gray', text = 'Box '+ self.number + '\n' + 'firma', command = lambda : openBoxWin(self, app))

    def newParking(self, ECV, firm, borr):
        if self.record is not None:
            self.record = self.createRecord(ECV, firm, borr)
            self.changeColor()

    def endParking(self):
        self.endRecord()
        self.record = None
        self.changeColor()

    def getColor(self):
        color = 'grey'
        if self.record is None:
            color = 'grey'
        else:
            if self.record.id_company == self.idCompany:
                color = 'green'
            else:
                if self.record.lended:
                    color = 'orange'
                else:
                    color = 'red'
                    
        return color
    def changeColor(self):
        self.button.config(bg = self.getColor())

    def createRecord(self, ECV, firm, borr):
        pass
        #vytvor instanciu záznamu a vrat ju

    def endRecord(self):
        pass
        #zrus instanciu záznamu
