from datetime import datetime

'''
Logger - Trieda, ktorá slúži na logovanie počas behu aplikácie
'''
class Logger:
    '''
    fileName - súbor, do ktorého sa logy zapisujú (defaultne 'log.txt')
    mode - môže mať dve hodnoty ('reset' alebo 'append')
         - pri 'reset' vymaže obsah zadaného súboru (najlepsie pri spusteni app)
         - pri 'append' obsah ponechá a zapisuje na koniec súboru
    '''
    def __init__(self, fileName="log.txt", mode="append"):
        self.fileName = fileName

        if(mode == "reset"):
            open(fileName, "w+")
            

    '''
    priváte metóda
    vypíše dátum vo formáte 'dd/mm/yyyy hh:mm:ss.fff'
    '''
    def __time(self):
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
        return "[{0}]".format(time)
    

    '''
    private metóda
    slúži na zapisovanie do zadaného súboru
    msg  - správa (log), ktorý chceme zapísať
    flag - vlajka, ktorou znázorňujeme dodatočnú dôležitosť
    '''
    def __write(self, msg, flag=""):
        textFile = open(self.fileName, "a+")

        line = "{0} {1:7} {2}\n".format(self.__time(), flag, msg)
        textFile.write(line)
        
        textFile.close()
        

    '''
    jednoduché logovanie
    '''
    def info(self, msg):
        self.__write(msg)
        

    '''
    logovanie chyby
    '''
    def error(self, msg):
        self.__write(msg, "ERROR")
        

    '''
    logovanie varovania
    '''
    def warning(self, msg):
        self.__write(msg, "WARNING")        
