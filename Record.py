class Record:
    def __init__(self, id, lended, id_company):
        self.id = id
        self.lended = lended
        self.ECV = ECV #dajte si ECV aj hore do initu
        self.id_company = id_company ##kto naozaj zaparkoval
        self.startParking = 'cas'
        self.endParking = 'cas'
        #!!!!!!!!!!!!!!!!dorobte si ktory box to bol!!!!!!!!!!!!!!!!!!!!!!!!!!
        # a nech sa vola boxID inak nebude fungovat statistika
        
    def save(self):
        pass
