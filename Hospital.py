import Doctor

class Hospital:

    peoplesRated = 0

    def __init__(self, nam, loc, rate="No reviews yet\n"):
        self.__name = nam
        self.__location = loc
        self.__rating = rate

    def rateMe(self,ratings):
        self.__rating = ((self.__rating * (self.peoplesVisited-1)) + ratings)/self.peoplesVisited
