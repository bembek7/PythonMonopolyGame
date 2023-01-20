from Field import Field
from Field import PropertyField
from Field import DiceChargeField
from Field import ChanceField
from Field import PayField
from Field import GoToJailField
from Property import Property
from Property import DiceChargeProperty
from Player import Player


def test_init():
    field = Field(0, "field")
    assert field.get_name() == "field"


def test_property():
    property = Property("property", 50, 100)
    field = PropertyField(0, property)
    assert field.get_property() == property


def test_buying():
    player = Player("player")
    player2 = Player("player2")
    property = Property("property", 50, 100)
    field = PropertyField(0, property)
    assert field.can_buy(player) is True
    field.buy(player2)
    assert field.can_buy(player) is False
    field.get_property().set_owner("")
    player.pay(1450)
    assert field.can_buy(player) is False


def test_property_action():
    player = Player("player")
    player2 = Player("player2")
    property = Property("property", 50, 0)
    field = PropertyField(0, property)
    field.buy(player)
    field.action(player2)
    assert player2.get_cash() == 1450
    assert player.get_cash() == 1550


def test_dice():
    player = Player("player")
    player2 = Player("player2")
    property = DiceChargeProperty("property", 10, 0, "dicecharge")
    field = DiceChargeField(0, property)
    field.buy(player)
    field.action(player2, 4)
    assert player2.get_cash() == 1480
    assert player.get_cash() == 1520


def test_chance():
    player = Player("player")
    field = ChanceField(0, "chance")
    field.action(player, 20)
    assert player.get_cash() == 1520
    field.action(player, -40)
    assert player.get_cash() == 1480


def test_pay():
    player = Player("player")
    field = PayField(0, "pay", 100)
    field.action(player)
    assert player.get_cash() == 1400


def test_jail():
    player = Player("player")
    field = GoToJailField(0, "gotojail")
    field.action(player)
    assert player.is_in_jail() is True
    assert player.get_position() == 10
