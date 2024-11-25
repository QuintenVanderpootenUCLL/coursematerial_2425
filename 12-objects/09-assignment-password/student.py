class Password:
    def __init__(self, string):
        self.__password = string
    
    def verify(self, string):
        return self.__password == string


        