class Patient:

    def __init__(self, name, contact, loc, query="COVID"):
        self.__name = name
        self.__contactNumber = contact
        self.__depart = query
        self.location = loc

    def getName(self):
        return self.__name

    def getContact(self):
        return self.__contactNumber

    def getDepart(self):
        return self.__depart


