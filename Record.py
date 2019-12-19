from Files import File
from Database import Database

class Record:
    def __init__(self, id, lended, ECV, idCompany, photoFileName = None):
        self.id = id
        self.lended = lended
        self.ECV = ECV
        self.idCompany = idCompany ##kto naozaj zaparkoval
        self.arrivalTime = 'cas'
        self.departureTime = 'cas'
        self.photoFileName = photoFileName

    def addPhoto(self):
        name = File.choosePhoto()
        self.photoFileName = name

    def save(self):
        createRecord(self)
        pass
