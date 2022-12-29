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
    
    def get_color(self):
        return self._color

    def buy_apartment(self):
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

    def get_type(self):
        return self._type

class AirportProperty(SpecialProperty):
    def charge(self):
        owning_other = self._owner.get_amount_of_type()
        if owning_other == 3:
            owning_other = 4
        elif owning_other == 4:
            owning_other = 8
        return self._basic_charge * owning_other
    
class DiceChargeProperty(SpecialProperty):
    def charge(self, dice_result):
        owning_other = self._owner.get_amount_of_type()
        if owning_other == 2:
            charge = self._basic_charge * dice_result
        else:
            charge = round(self._basic_charge * dice_result / 2)
        return charge