import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

##docasna funkcia len
def find(arr, key):
    for i in arr:
        if i[1] == int(key):
            if(len(i[0]) > 8):
                return i[0][0:8]+'..'
            else:
                return i[0]
    return 'NIC'

class FrameParking:
    def __init__(self, nb, sizePerc, app):
        self.frame = tk.Frame(nb)
        nb.add(self.frame, text = "Parkovisko")
        
        self.canvas = Canvas(self.frame, width = sizePerc[0], height = sizePerc[1])
        self.canvas.pack(side = 'left')
        self.canvas.pack_propagate(0)
        self.notifications = ['Box c. 15 konci.', 'Box c. 5 konci',
            'Box c. 3435 konci', 'Box c. 6543 konci']
        self.lb = Listbox(self.frame, relief = SUNKEN)
        for i in self.notifications:
            self.lb.insert(END, i)
        self.lb.bind("<<ListboxSelect>>", onClickOnNotification)
        self.lb.pack(side = 'right')        

        firmy = [('KVANT',0),('Integard',1),('KVANTN',3),('skola.sk',4),('D4R7',5),('MKMs',6),('MTRUST',7),('BusinessMedia',8),('RESTAURACIA',9),('NIKTO',10)]
        t = open('konfig-parkoviska.txt', 'r')
        riadok = t.readline()
        print(riadok)
        while riadok != '':
            r = riadok.split(';')
            tk.Button(self.canvas,bg = 'gray', text = 'Box '+str(r[1])+'\n'+find(firmy,r[6]), command = lambda : openBoxWin('1', app)).place(x = int(float(r[2])), y = int(float(r[3])), width = int(float(r[4])),height = int(float(r[5])))
            riadok = t.readline()
        t.close()

##                print('teraz napisem ')
##        print(sizePerc)
##
##        pocetHorizontlane = 12
##        pocetVertikalne = 3
##        medzeraMedziBoxami = 10
##        wi = (sizePerc[0] - 2* 50 - (pocetHorizontlane * medzeraMedziBoxami))/pocetHorizontlane 
##        he = (sizePerc[1] - 2 * 50 - (pocetVertikalne * medzeraMedziBoxami))/pocetVertikalne
##        print(wi)
##        print(he)
##        self.canvas.create_rectangle(1070, 620, 1072, 622, fill='red')
##        
##        xkova = 50
##        ypsilonkova = 50

##        for i in listSuradnic:
##            xkova = i[0]
##            ypsilonkova = i[1]
##            #print(str(xkova)+';'+str(ypsilonkova)+';'+str(wi)+';'+str(he)+';')
##            tk.Button(self.canvas,bg = 'gray', text = 'Box '+str(2)+',\nLampy.sk', command = lambda : openBoxWin('1', app)).place( height = int(he), width = int(wi), x = xkova, y = ypsilonkova,)
##          
##        for y in range(3):
##            for x in range(12):
##                #print('('+str(xkova)+', '+str(ypsilonkova)+'),')
##                tk.Button(self.canvas,bg = 'gray', text = 'Box '+str(x)+',\nLampy.sk', command = lambda : openBoxWin('1', app)).place( height = int(he), width = int(wi), x = xkova, y = ypsilonkova,)
##                xkova += wi + medzeraMedziBoxami
##            xkova = 50
##            ypsilonkova += he + medzeraMedziBoxami
        
class FrameStatistic:
    def __init__(self, nb, sizePerc):
        self.frame = tk.Frame(nb)
        nb.add(self.frame, text="Štatistika")

        self.canvas = Canvas(self.frame,  width = sizePerc[0], height = sizePerc[1])
        self.canvas.pack(anchor='c')
        self.canvas.pack_propagate(0)

        fr1 = tk.Frame(self.canvas)
        fr1.pack(pady=5)
        ecvPorusujuceParkovani = ttk.Checkbutton(fr1, text = 'EČV porušujúce parkovanie')
        ecvPorusujuceParkovani.pack(anchor='w')
        ecvPorusujuceParkovaniSucetCasu = ttk.Checkbutton(fr1, text = 'súčet času')
        ecvPorusujuceParkovaniSucetCasu.pack(padx=20, anchor='w')
        ecvPorusujuceParkovaniPocetZaznamov = ttk.Checkbutton(fr1, text = 'počet záznamov')
        ecvPorusujuceParkovaniPocetZaznamov.pack(padx=20, anchor='w')

        fr2 = tk.Frame(self.canvas)
        fr2.pack(pady=10)
        firmyPorusujuceParkovani = ttk.Checkbutton(fr2, text = 'Firmy porušujúce parkovanie')
        firmyPorusujuceParkovani.pack(anchor='w')
        firmyPorusujuceParkovaniSucetCasu = ttk.Checkbutton(fr2, text = 'súčet času')
        firmyPorusujuceParkovaniSucetCasu.pack(padx=20, anchor='w')
        firmyPorusujuceParkovaniPocetZaznamov = ttk.Checkbutton(fr2, text = 'počet záznamov')
        firmyPorusujuceParkovaniPocetZaznamov.pack(padx=20, anchor='w')

        fr3 = tk.Frame(self.canvas)
        fr3.pack(pady=10)
        obsadenostBoxov = ttk.Checkbutton(fr3, text = 'Obsadenosť boxov')
        obsadenostBoxov.pack(anchor='w')
        obsadenostBoxovKazdyBox = ttk.Checkbutton(fr3, text = 'každý box')
        obsadenostBoxovKazdyBox.pack(padx=20, anchor='w')
        
        frameTime = tk.Frame(fr3)
        frameTime.pack(padx=20, anchor='w')
        obsadenostBoxovKazdyBoxVCase = ttk.Checkbutton(frameTime, text = 'každý box v čase ')
        obsadenostBoxovKazdyBoxVCase.pack(side = 'left')
        
        fromHour = ttk.Combobox(frameTime, values = [i for i in range(1,24)], width = 3)
        fromHour.pack(side = 'left')        
        fromHour.pack_propagate(0)
        labelDvojbodka1 = tk.Label(frameTime, text = ' : ')
        labelDvojbodka1.pack(side = 'left')
        fromMinute = ttk.Combobox(frameTime, values = [i for i in range(00,60)], width = 3)
        fromMinute.pack(side = 'left')
        fromMinute.pack_propagate(0)
        labelPomlcka = tk.Label(frameTime, text = ' - ')
        labelPomlcka.pack(side = 'left')
        toHour = ttk.Combobox(frameTime, values = [i for i in range(1,24)], width = 3)
        toHour.pack(side = 'left')
        toHour.pack_propagate(0)
        labelDvojbodka2 = tk.Label(frameTime, text = ' : ')
        labelDvojbodka2.pack(side = 'left')
        toMinute = ttk.Combobox(frameTime, values = [i for i in range(00,60)], width = 3)
        toMinute.pack(side = 'left')
        toMinute.pack_propagate(0)

        fr4 = tk.Frame(self.canvas)
        fr4.pack(pady=10)
        vyuzivaniemiestaPreZtp = ttk.Checkbutton(fr4, text = 'Využívanie miesta pre ZŤP')
        vyuzivaniemiestaPreZtp.pack(anchor='w')
        vyuzivaniemiestaPreZtpKazdyBox = ttk.Checkbutton(fr4, text = 'každý box')
        vyuzivaniemiestaPreZtpKazdyBox.pack(padx=20, anchor='w')
        vyuzivaniemiestaPreZtpPodlaFiriem = ttk.Checkbutton(fr4, text = 'podľa firiem')
        vyuzivaniemiestaPreZtpPodlaFiriem.pack(padx=20, anchor='w')  

        buttonGenerate = ttk.Button(self.canvas, text='Vygeneruj')
        buttonGenerate.pack()
        
class FrameNajomnici:
    def __init__(self, nb, sizePerc):
        self.frame = tk.Frame(nb)
        nb.add(self.frame, text="Nájomníci")

        self.canvas = Canvas(self.frame, width = sizePerc[0], height = sizePerc[1])
        self.canvas.pack(anchor='c')
        self.canvas.pack_propagate(0)
        
        fr2 = Frame(self.canvas)
        fr2.pack(side='left',padx=30, pady=20)
        
        label = ttk.Label(fr2, text='Zoznam nájomníkov:')
        label.pack(padx = 5, pady = 5)
        
        fr21 = Frame(fr2)
        fr21.pack(padx = 10, pady = 10)

        fr3 = Frame(self.canvas)
        fr3.pack(side='right', padx=5)
        
        self.najomnici = ['Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo']
        self.lb = Listbox(fr21, relief=SUNKEN)
        for i in self.najomnici:
            self.lb.insert(END, i)
        #self.lb.bind("<<ListboxSelect>>", onClickOnNotification)

        scr = Scrollbar(fr21, command = self.lb.yview)
        scr.pack(side = RIGHT, fill = Y)
        
        self.lb.config(yscrollcommand=scr.set)
        self.lb.pack(side='left')
        
        buttonRemoveNajomnika = ttk.Button(fr2, text='Odstráň', command = lambda: removeNajomnika(self.lb.get(ACTIVE)))
        buttonRemoveNajomnika.pack(padx = 5, pady = 5)        

        self.entry = Entry(fr3)        
        self.entry.insert(0, 'Zadaj firmu.')
        self.entry.pack(padx = 5, pady = 5)

        #self.entry.get()
        buttonAddNajomnika = ttk.Button(fr3, text='Pridaj', command = lambda: addNajomnika(self.entry.get()))
        buttonAddNajomnika.pack(padx = 5, pady = 5)
        
        buttonSaveChanges = ttk.Button(fr3, text='Ulož')
        buttonSaveChanges.pack(side='bottom', padx = 5, pady = 40)

## pomocne funkcie
def openBoxWin(idcko, app):
    print('openBoxWin(), id: ', idcko)
    currentBox = BoxWindow(idcko,app)

def removeNajomnika(var):
    print('removeNajomnika')
    print(' ', var)

def addNajomnika(var):
    print('addNajomnika')
    print(' ', var)

def onClickOnNotification(val):
    print(val)
    pass

def getSizeForPercent(main, percento):
    width = (main.winfo_screenwidth()  // 100) * percento
    height =  (main.winfo_screenheight() // 100) * percento
    return (width, height)

class BoxWindow:
    def __init__(self, idcko, app):
        self.win = Tk()
        self.win.title('Box')
        sizePerc = getSizeForPercent(app, 60)
        self.win.geometry('{}x{}'.format(sizePerc[0], sizePerc[1]))

        self.canvas = Canvas(self.win, width = sizePerc[0]-100, height = sizePerc[1]-100)
        self.canvas.pack(anchor='c')

        label = ttk.Label(self.canvas, text='Parkovací box '+idcko)
        label.pack(padx = 5, pady = 10)

        labelEcv = ttk.Label(self.canvas, text='ECV: BA 123GB')
        labelEcv.pack(padx = 5, pady = 10)

        startTime = ttk.Label(self.canvas, text='Začiatok parkovania: 00:00')
        startTime.pack(padx = 5, pady = 10)

        firma = ttk.Label(self.canvas, text='Firma: Lampy.sk')
        firma.pack(padx = 5, pady = 10)

        typParkovania = ttk.Label(self.canvas, text='Zapožičané')
        typParkovania.pack(padx = 5, pady = 10)

        buttonNahratFotku = tk.Button(self.canvas, text = 'Nahrať fotku')
        buttonNahratFotku.pack(padx = 5, pady = 10)

        buttonUkoncitParkovanie = tk.Button(self.canvas, text = 'Ukončiť parkovanie fotku')
        buttonUkoncitParkovanie.pack(padx = 5, pady = 10)
        
class NewBoxWindow:
    def __init__(self, idcko, app):
        self.win = Tk()
        self.win.title('Box')
        sizePerc = getSizeForPercent(app, 60)
        self.win.geometry('{}x{}'.format(sizePerc[0], sizePerc[1]))

        self.canvas = Canvas(self.win, background = 'navy', width = sizePerc[0]-100, height = sizePerc[1]-100)
        self.canvas.pack(anchor='c')

        label = ttk.Label(self.canvas, text='Parkovací box '+idcko)
        label.pack(padx = 5, pady = 5)

        entryECV = Entry(self.canvas)
        entryECV.pack()

        najomnici = ['Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo','Lampy.sk', 'Malovanky', 'Kroksovo', 'Kosovo', 'Losovo']
       
        comboBoxFirmy = ttk.Combobox(self.canvas, values = najomnici)
        comboBoxFirmy.pack()
        
        checkBoxBorowed = ttk.Checkbutton(self.canvas, text = 'Zapožičané')
        checkBoxBorowed.pack()

        buttonNahradFotku = ttk.Button(self.canvas, text='Nahrať fotku')
        buttonNahradFotku.pack()

        buttonNahradFotku = ttk.Button(self.canvas, text='Povrdiť')
        buttonNahradFotku.pack()
        
        self.win.mainloop()
        
class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.window()
        
        self.nb = ttk.Notebook(self.app)
        self.nb.pack()
        
        self.parkovisko = FrameParking(self.nb, getSizeForPercent(self.app, 90), self.app)
        self.statistiky = FrameStatistic(self.nb, getSizeForPercent(self.app, 60))
        self.najomnici = FrameNajomnici(self.nb, getSizeForPercent(self.app, 45))

        self.app.mainloop()
        
    def window(self):
        self.app.title('Parkovací systém')
        self.app.geometry('{}x{}'.format(self.app.winfo_screenwidth(), self.app.winfo_screenheight()))


main = MainWindow()
