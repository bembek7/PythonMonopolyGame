from Property import Property
from Player import Player


class Field:
    def __init__(self, position, name="") -> None:
        self._position = position
        self._name = name

    def get_name(self):
        return self._name

    def action(self, player):
        pass

    def can_buy(self, player: Player):
        return False


class PropertyField(Field):
    def __init__(self, position, property: Property) -> None:
        super().__init__(position, property.get_name())
        self._property = property

    def get_property(self):
        return self._property

    def can_buy(self, player: Player):
        if self._property.get_owner() is None:
            return player.can_afford(self._property.get_price())
        else:
            return False

    def action(self, player: Player):
        if self._property.get_owner() is not None and self._property.get_owner() != player:
            player.pay(self._property.charge())
            self._property.get_owner().gain(self._property.charge())

    def buy(self, player: Player):
        player.buy_property(self._property)


class DiceChargePropertyField(PropertyField):
    def action(self, player: Player, dice_result):
        if self._property.get_owner() is not None and self._property.get_owner() != player:
            player.pay(self._property.charge(dice_result))
            self._property.get_owner().gain(self._property.charge(dice_result))


class ChanceField(Field):
    def action(self, player, result):
        if result < 0:
            player.pay(abs(result))
        else:
            player.gain(result)


class PayField(Field):
    def __init__(self, position, name, amount_to_pay) -> None:
        super().__init__(position, name)
        self._amount_to_pay = amount_to_pay

    def action(self, player):
        player.pay(self._amount_to_pay)


class GoToJailField(Field):
    def action(self, player: Player):
        player.set_position(10)
        player.imprison()
