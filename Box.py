import tkinter as tk
from Record import Record
class Box:
    def __init__(self, id, number,  id_company, c, app, record = None):
        self.id = id
        self.number = number
        self.id_company = id_company #kto to ma zapozicane
        self.record = record
        self.button = tk.Button(c, bg = 'gray', text = 'Box '+ self.number + '\n' + 'firma', command = lambda : openBoxWin(self, app))

    def changeColor(self):
        self.button.config(bg = 'pink')
    #TODO
    def getBoxColor(self):
        if self.record is None:
            return 'grey'
        if self.record.lended:
            return 'orange'

from GUI import openBoxWin
