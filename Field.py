from Property import Property
from Player import Player


class Field:
    """
    A base class to represent field on a board.

    ...

    Attributes
    ----------
    position : int
        the position of the field on the board.
    name : str
        the name of the field.

    Methods
    -------
    get_name()
        returns the name of the field
    action(player: Player)
        to be overloaded by children
    can_buy(player: Player)
        to be overloaded by children
    """
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
    """
    A class to represent a PropertyField inheriting from Field class.

    ...

    Attributes
    ----------
    position : int
        the position of the field on the board.
    name : str
        the name of the field.
    property : Property
        the property associated with the field

    Methods
    -------
    get_name()
        returns the name of the field
    action(player: Player)
        charge the player if the property is owned by another player
    can_buy(player: Player)
        returns a boolean indicating if player can buy the property.
    buy(player: Player)
        calls the method on player to buy property associated with the field
    """
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
        owner = self._property.get_owner()
        if owner is not None and owner != player:
            player.pay(self._property.charge())
            owner.gain(self._property.charge())

    def buy(self, player: Player):
        player.buy_property(self._property)


class DiceChargeField(PropertyField):
    """
    A class to represent a DiceChargeField inheriting from PropertyField class.

    ...

    Attributes
    ----------
    position : int
        the position of the field on the board.
    name : str
        the name of the field.
    property : Property
        the property associated with the field

    Methods
    -------
    get_name()
        returns the name of the field
    action(player: Player)
        charges the player, using dice result as multiplier
    can_buy(player: Player)
        returns a boolean indicating if player can buy the property.
    buy(player: Player)
        calls the method on player to buy property associated with the field
    """
    def action(self, player: Player, dice_result):
        owner = self._property.get_owner()
        if owner is not None and owner != player:
            player.pay(self._property.charge(dice_result))
            owner.gain(self._property.charge(dice_result))


class ChanceField(Field):
    """
    A class for field that represents a chance field.
    Inherits from Field class.

    ...

    Methods
    -------
    action(player: Player, result)
        make the player lose or win amount of money that gets as a "result".
    """
    def action(self, player, result):
        if result < 0:
            player.pay(abs(result))
        else:
            player.gain(result)


class PayField(Field):
    """
    A class for field that requires the player to pay money on landing
    Inherits from Field class.

    ...

    Attributes
    ----------
    _amount_to_pay : int
        the amount that the player must pay.

    Methods
    -------
    action(player: Player)
        makes the player pay the specified amount.
    """
    def __init__(self, position, name, amount_to_pay) -> None:
        super().__init__(position, name)
        self._amount_to_pay = amount_to_pay

    def action(self, player):
        player.pay(self._amount_to_pay)


class GoToJailField(Field):
    """
    A field that represents a "go to jail" field on the board
    Inherits from Field class.

    ...

    Methods
    -------
    action(player: Player)
        moves the player to the jail field and imprisons them.
    """
    def action(self, player: Player):
        player.set_position(10)
        player.imprison()
