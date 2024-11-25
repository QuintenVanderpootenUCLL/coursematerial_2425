class Counter:
    def __init__(self):
        self.count = 0

    @property
    def count(self):
        self.count

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0