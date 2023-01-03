from Property import Property
from Property import TypicalProperty
from Property import SpecialProperty
# pieniądze
# lista posiadlosci


class Player:
    def __init__(self, name) -> None:
        self._name = name
        self._cash = 1500
        self._position = 0
        self._properties = []
        self._in_jail = False
        self._dir_of_colors = {
            "brown": 0,
            "light blue": 0,
            "pink": 0,
            "orange": 0,
            "red": 0,
            "yellow": 0,
            "green": 0,
            "dark blue": 0
        }
        self._dir_of_colors_needed = {
            "brown": 2,
            "light blue": 3,
            "pink": 3,
            "orange": 3,
            "red": 3,
            "yellow": 3,
            "green": 3,
            "dark blue": 2
        }

    def get_properties(self):
        return self._properties

    def get_cash(self):
        return self._cash

    def get_position(self):
        return self._position

    def set_position(self, newposition):
        self._position = newposition

    def get_in_jail(self):
        return self._in_jail

    def set_in_jail(self, setjail):
        self._in_jail = setjail

    def get_name(self):
        return self._name

    def gain(self, amount):
        self._cash = int(self._cash + amount)

    def get_activable_properties(self):
        activable_apartments = []
        return activable_apartments

    def get_deactivable_properties(self):
        deactivable_apartments = []
        return deactivable_apartments

    def get_sellable_apartments(self):
        sellable_apartments = []
        for property in self._properties:
            if isinstance(property, TypicalProperty):
                if property.get_apartments_nr() > 0:
                    color = property.get_color()
                    apartments_nr = property.get_apartments_nr()
                    if self.can_sell_apartment_on_property(color, apartments_nr):
                        sellable_apartments.append(property)
        return sellable_apartments

    def get_available_apartments(self):
        available_apartments = []
        if self.can_buy_apartment():
            for property in self._properties:
                if property.is_active():
                    if isinstance(property, TypicalProperty):
                        if property.get_apartments_nr() < 5:
                            color = property.get_color()
                            apartments_nr = property.get_apartments_nr()
                            if self.can_apartment_property(color, apartments_nr):
                                available_apartments.append(property)
        return available_apartments

    def can_sell_apartment_on_property(self, color, apartments_nr):
        other = 0
        for property in self._properties:
            if isinstance(property, TypicalProperty):
                if property.is_active():
                    if property.get_color() == color:
                        if property.get_apartments_nr() <= apartments_nr:
                            other += 1
        return other == self._dir_of_colors_needed[color]

    def can_apartment_property(self, color, apartments_nr):
        other = 0
        for property in self._properties:
            if isinstance(property, TypicalProperty):
                if property.is_active():
                    if property.get_color() == color:
                        if property.get_apartments_nr() >= apartments_nr:
                            other += 1
        return other == self._dir_of_colors_needed[color]

    def pay(self, amount):
        if self._cash - amount >= 0:
            self._cash = int(self._cash - amount)
        return True
    # wymuszenie zastawu/sprzedaży

    def buy_apartment(self, property):
        self.pay(int(property.get_apartment_price()))
        property.get_apartment()

    def sell_apartment(self, property):
        self.gain(int(property.get_apartment_price())/2)
        property.lose_apartment()

    def get_available_deactivations(self):
        pass

    def deactivate_property(self, property_given):
        for property in self._properties:
            if property.get_name() == property_given and property.is_active():
                property.deactivate()
                self.gain(int(property.get_price() / 2))

    def get_amount_of_type(self, type):
        result = 0
        for property in self._properties:
            if isinstance(property, SpecialProperty):
                if property.get_type() == type:
                    result += 1
        return result

    def buy_property(self, property: Property):
        self._properties.append(property)
        if isinstance(property, TypicalProperty):
            self._dir_of_colors[property.get_color()] += 1
        self.pay(property.get_price())

    def move(self, result):
        board_places = 40
        if self._position + result >= board_places:
            self._cash += 200
        if self._position + result < 0:
            self._position = board_places + self._position + result
        self._position = (self._position + result) % board_places

    def can_buy_apartment(self):
        for key in self._dir_of_colors:
            if self._dir_of_colors[key] == self._dir_of_colors_needed[key]:
                return True
            return False
