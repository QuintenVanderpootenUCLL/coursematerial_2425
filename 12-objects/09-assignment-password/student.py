class Password:
    def __init__(self, string):
        self.__password = string
    
    def verify(self, string):
        return self.__password == string

password = Password('azer1234')
print(password.verify('qwer1234'))
print(password.verify('azer1234'))