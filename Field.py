from Property import Property
from Player import Player


class Field:
    def __init__(self, position, name = "") -> None:
        self._position = position
        self._name = name

    def get_name(self):
        return self._name

    def Action(self):
        pass

class PropertyField(Field):
    def __init__(self, position, property: Property) -> None:
        super().__init__(position, property.get_name())
        self._property = property

    def get_property(self):
        return self._property

    def Action(self, player: Player):
        if self._property.get_owner() != "":
            if player.pay(self._property.get_price()):
                player.buy_property(self._property)
                self._property.set_owner(player.get_name())
        else:
            player.pay(self._property.charge())

class ChanceField(Field):
    def __init__(self, position, name="") -> None:
        super().__init__(position, name)
    def Action(self, player):
        pass

class PayField(Field):
    def __init__(self, position, name, amount_to_pay) -> None:
        super().__init__(position, name)
        self._amount_to_pay = amount_to_pay
    def Action(self, player):
        player.pay(self._amount_to_pay)

class GoToJailField(Field):
    def Action(self, player : Player):
        player.set_position(10) #
        player.set_in_jail(True)