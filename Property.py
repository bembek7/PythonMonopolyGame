class Property:
    def __init__(self, name, basic_charge, price) -> None:
        self._name = name
        self._basic_charge = basic_charge
        self._owner = ""
        self._price = price
        self._active = True

    def is_active(self):
        return self._active

    def deactivate(self):
        self._active = False

    def activate(self):
        self._active = True

    def __str__(self) -> str:
        return self._name

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
        self._apartments = 1  # 6 = hotel
        self._apartment_price = apartment_price

    def get_color(self):
        return self._color

    def get_apartment(self):
        if self._apartments < 6:
            self._apartments += 1

    def get_apartments_nr(self):
        return self._apartments - 1

    def get_apartment_price(self):
        return self._apartment_price

    def charge(self):
        if self._active:
            return self._basic_charge * self._apartments
        else:
            return 0


class SpecialProperty(Property):
    def __init__(self, name, basic_charge, price, type) -> None:
        super().__init__(name, basic_charge, price)
        self._type = type

    def get_type(self):
        return self._type


class AirportProperty(SpecialProperty):
    def charge(self):
        if self._active:
            owning_other = self._owner.get_amount_of_type(self._type)
            if owning_other == 3:
                owning_other = 4
            elif owning_other == 4:
                owning_other = 8
            return self._basic_charge * owning_other
        else:
            return 0


class DiceChargeProperty(SpecialProperty):
    def charge(self, dice_result):
        if self._active:
            owning_other = self._owner.get_amount_of_type()
            if owning_other == 2:
                charge = self._basic_charge * dice_result
            else:
                charge = round(self._basic_charge * dice_result / 2)
            return charge
        else:
            return 0
