class Averager:
    def __init__(self):
        self.count = 0
        self.sum = 0
    
    def add(self, number):
        self.count += 1
        self.sum += number
    
    def average(self):
        return self.sum / self.count
    
    def reset(self):
        self.count = 0
        self.sum = 0
    
