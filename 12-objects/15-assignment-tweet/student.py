class Tweet:
    def __init__(self, message, max_length):       
        self.__message = message
        self.max_length = max_length
        
    
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, new_message):
        if len(new_message) > self.__max_length:
            self.__message = new_message[0:self.__max_length]
        else:
            self.__message = new_message
    
    @property
    def max_length(self):
        return self.__max_length
    
    @max_length.setter
    def max_length(self, number):
        if number < 1:
            raise ValueError("waarde van max_length moet groter zijn dan 1")
        self.__max_length = number

        if len(self.message) > self.max_length:
            self.message = self.message[0:self.max_length]



tweet = Tweet("1234567", 10)
print(tweet.message)

tweet = Tweet("1234567", 5)
print(tweet.message)

tweet.max_length = 20
print(tweet.message)

tweet.max_length = 3
print(tweet.message)

#tweet.max_length = 0

