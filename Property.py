#buying
class Property:
    def __init__(self, name, basic_charge, price) -> None:
        self._name = name
        self._basic_charge = basic_charge
        self._owner = ""
        self._price = price

    def get_owner(self):
        return self._owner

    def set_owner(self, players_name):
        self._owner = players_name
    
    def get_name(self):
        return self._name

    def charge(self):
        return self._basic_charge

    def get_price(self):
        return self._price


class TypicalProperty(Property):
    def __init__(self, name, basic_charge, price, color, apartment_price) -> None:
        super().__init__(name, basic_charge, price)
        self._color = color
        self._apartments = 1 # 6 = hotel
        self._apartment_price = apartment_price
    
    def gain_apartment(self):
        if(self._apartments <5):
            self._apartments += 1
        # dodanie bloku na rushowanie jednego pola

    def get_apartment_prize(self):
        return self._apartment_price

    def charge(self):
        return self._basic_charge * self._apartments


class SpecialProperty(Property):
    def __init__(self, name, basic_charge, price, type) -> None:
        super().__init__(name, basic_charge, price)
        self._type = type

    def charge(self, multiplicator):
        return multiplicator * self._basic_charge