class Unit:
    def __init__(self, health, firepower, armor):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError("de waarden moeten positief zijn!!")
        self.__health = health
        self.__firepower = firepower
        self.__armor = armor

    @property
    def health(self):
        return self.__health
    @property
    def firepower(self):
        return self.__firepower
    @property
    def armor(self):
        return self.__armor

    @health.setter
    def health(self, number):
        self.__health = number
    
    def shot_by(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Dit is geen Unit Class")
        damage = other.firepower - self.armor
        if damage > 0:
            self.health -= damage
        if self.health < 0:
            self.health = 0


unit1 = Unit(100, 20, 10) 
unit2 = Unit(50, 15, 5) 
unit1.shot_by(unit2) 
print(unit1.health)

    
