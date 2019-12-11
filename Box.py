import tkinter as tk

class Box:
    def __init__(self, id, cislo, x, y, sirka, vyska, id_firmy, c, app, zaznam = None):
        self.id = id
        self.cislo = cislo
        self.id_firmy = id_firmy #kto to ma zapozicane
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska
        self.zaznam = zaznam
        self.button = tk.Button(c, bg = 'gray', text = 'Box '+ self.cislo + '\n' + 'firma', command = lambda : openBoxWin(self, app))

    def changeColor(self):
        self.button.config(bg = 'pink')

    def getBoxColor(self):
        if self.zaznam is None:
            return 'grey'
        if self.zaznam.zapozicany:
            return 'orange'

class Zaznam:
    def __init__(self):
        self.id = id
        self.obsadeny = obsadeny
        self.zapozicany = zapozicany
        self.ECV = ECV
        self.id_firma = id_firma ##kto naozaj zaparkoval
        
    def uloz(self):
        pass

from GUI import openBoxWin
