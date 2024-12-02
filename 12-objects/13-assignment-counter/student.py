class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count
    

    @count.setter
    def count(self, value):
        self._count = value

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0


counter = Counter()
print(counter.count)

counter.increment()
print(counter.count)
counter.increment()
print(counter.count)
counter.reset()
print(counter.count)