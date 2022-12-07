# cena, // domki, hotele
# owner
# nazwa
class Property:
    def __init__(self, name, position, basiccharge) -> None:
        self._name = name
        self._position = position
        self._basiccharge = basiccharge
        self._owner = ""

    def set_owner(self, name):
        owner = name


class TypicalProperty(Property):
    def __init__(self, name, position, basiccharge, color, apartment_prize) -> None:
        super().__init__(name, position, basiccharge)
        self._color = color
        self._apartments = 0 # 5 = hotel
        self._apartment_prize = apartment_prize
    
    def gain_apartment(self):
        if(self._apartments <5):
            self._apartments += 1
        # dodanie bloku na rushowanie jednego pola

    def get_apartment_prize(self):
        return self._apartment_prize

    def charge(self):
        return max(self._basic_charge, self._basic_charge * self._apartments)


class TypicalProperty(Property):
    def __init__(self, name, position, basiccharge, type, apartment_prize) -> None:
        super().__init__(name, position, basiccharge)
        self._type = type

    
    def gain_apartment(self):
        if(self._apartments <5):
            self._apartments += 1
        # dodanie bloku na rushowanie jednego pola

    def special_charge(self, multiplicator):
        return multiplicator * self._basiccharge