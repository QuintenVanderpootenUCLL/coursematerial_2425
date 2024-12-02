class Interval:
    def __init__(self, lower, upper):
        self.upper = upper
        self.lower = lower
    
    def is_empty(self):
        return self.lower > self.upper
    
    def contains(self, number):
        return self.lower <= number and self.upper >= number
            
    def overlaps_with(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Dit is geen interval object")
        if self.is_empty() or other.is_empty():
            return False
        elif (self.lower <= other.upper and self.lower >= other.lower) or (other.lower <= self.upper and other.lower >= self.lower):
            return True
        else:
            return False