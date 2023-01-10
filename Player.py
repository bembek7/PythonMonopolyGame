from Property import Property
from Property import TypicalProperty
from Property import SpecialProperty


class Player:
    """
    A class to represent a player.

    ...

    Attributes
    ----------
    name : str
        name of the player
    cash : int
        cash amount of the player
    position : int
        position of the player
    properties : array
        properties of theplayer
    in_jail : bool
        if player is in a jail
    rounds_left : int
        rounds left for player in a jail
    dir_of_colors : dict
        what properties of colors player has
    dir_of_colors_needed : dict
        what properties of colors player need to apartment

    Methods
    -------
    decrement_rounds():
        Decrement the number of rounds the player has left to be in jail by one.
    get_rounds_left():
        Returns the number of rounds left for the player to serve in jail.
    imprison():
        Imprison the player, setting the player in jail and resetting the rounds_left to 3
    free():
        Free the player, setting the player no longer in jail
    can_afford(amount: int) -> bool:
        Check if the player can afford a given amount of cash.
    lose():
        Removes the player from the game, losing all of their properties
    lose_property(property: Property):
        Removes a given property from an array of player Properties
    """

    def __init__(self, name) -> None:
        self._name = name
        self._cash = 1500  # zmienic po testach
        self._position = 0
        self._properties = []
        self._in_jail = False
        self._rounds_left = 0
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

    def decrement_rounds(self):
        self._rounds_left -= 1

    def get_rounds_left(self):
        return self._rounds_left

    def imprison(self):
        self._in_jail = True
        self._rounds_left = 3

    def free(self):
        self._in_jail = False

    def is_in_jail(self):
        return self._in_jail

    def is_broke(self):
        return self._cash < 0

    def get_properties(self):
        return self._properties

    def get_cash(self):
        return self._cash

    def get_position(self):
        return self._position

    def set_position(self, newposition):
        self._position = newposition

    def get_name(self):
        return self._name

    def can_afford(self, amount):
        return self._cash >= amount

    def lose(self):
        for property in self._properties:
            property.free()
        del self

    def gain(self, amount):
        self._cash = int(self._cash + amount)

    def lose_property(self, property):
        self._properties.remove(property)

    def gain_property(self, property):
        self._properties.append(property)
        property.set_owner(self)

    def get_sellable_properties(self):
        sellable_properties = []
        for property in self._properties:
            if self.check_other_apartments(property):
                sellable_properties.append(property)
        return sellable_properties

    def get_activable_properties(self):
        activable_apartments = []
        for property in self._properties:
            if not property.is_active():
                activable_apartments.append(property)
        return activable_apartments

    def get_deactivable_properties(self):
        deactivable_apartments = []
        for property in self._properties:
            if property.is_active():
                if not isinstance(property, TypicalProperty):
                    deactivable_apartments.append(property)
                elif property.get_apartments_nr() == 0:
                    color = property.get_color()
                    if self.check_other_apartments(color):
                        deactivable_apartments.append(property)
        return deactivable_apartments

    def check_other_apartments(self, property):
        if isinstance(property, TypicalProperty):
            color = property.get_color()
            for property in self._properties:
                if isinstance(property, TypicalProperty):
                    if property.get_color() == color and property.get_apartments_nr() > 0:
                        return False
        return True

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
        self._cash = int(self._cash - amount)

    def buy_apartment(self, property):
        self.pay(int(property.get_apartment_price()))
        property.get_apartment()

    def sell_apartment(self, property):
        self.gain(int(property.get_apartment_price()) / 2)
        property.lose_apartment()

    def deactivate_property(self, property):
        if property.is_active():
            property.deactivate()
            self.gain(int(property.get_price() / 2))

    def activate_property(self, property):
        if not property.is_active():
            property.activate()
            self.pay(int(property.get_price() / 2 + property.get_price() / 10))

    def get_amount_of_type(self, type):
        result = 0
        for property in self._properties:
            if isinstance(property, SpecialProperty):
                if property.get_type() == type:
                    result += 1
        return result

    def buy_property(self, property: Property):
        self._properties.append(property)
        property.set_owner(self)
        if isinstance(property, TypicalProperty):
            self._dir_of_colors[property.get_color()] += 1
        self.pay(property.get_price())

    def move(self, result):
        board_places = 40
        if not self._in_jail:
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
