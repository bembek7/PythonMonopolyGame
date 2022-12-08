from Property import Property
from Player import Player


class Field:
    def __init__(self, postion, name = "") -> None:
        self._position = postion
        self._name = name

    def Action(self):
        pass

class PropertyField(Field):
    def __init__(self, postion, property: Property) -> None:
        super().__init__(postion, property.get_name())
        self._property = property

    def Action(self, player: Player):
        if self._property.get_owner() != "":
            player.pay(self._property.get_price())
        else:
            player.pay(self._property.charge())

class SpecialField(Field):
    def Action(self, player, action):
        # special actions will be implemented
        pass