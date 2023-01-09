from Property import Property
from Property import TypicalProperty
from Property import DiceChargeProperty
from Property import AirportProperty
from Player import Player


def test_init():
    property = Property("property", 50, 100)
    assert property.charge() == 50
    assert property.get_price() == 100
    assert property.get_owner() == ""
    assert property.is_active() is True
    assert property.get_name() == "property"


def test_activation():
    property = Property("property", 50, 100)
    property.deactivate()
    assert property.is_active() is False
    assert property.charge() == 0
    property.activate()
    assert property.is_active() is True
    assert property.charge() == 50


def test_str():
    property = Property("property", 50, 100)
    property.__str__() == "property"


def test_ownership():
    property = Property("property", 50, 100)
    assert property.get_owner() == ""
    property.set_owner("nazwa")
    assert property.get_owner() == "nazwa"
    property.free()
    assert property.get_owner() == ""


def test_typical_free():
    property = TypicalProperty("property", 50, 100, "brown", 50)
    assert property.get_color() == "brown"
    property.get_apartment()
    assert property.get_apartments_nr() == 1
    property.free()
    assert property.get_apartments_nr() == 0


def test_typical_apartmenting():
    property = TypicalProperty("property", 50, 100, "brown", 50)
    property.get_apartment()
    assert property.get_apartments_nr() == 1
    property.lose_apartment()
    assert property.get_apartments_nr() == 0
    assert property.get_apartment_price() == 50


def test_typical_charging():
    property = TypicalProperty("property", 4, 100, "brown", 50)
    property.get_apartment()
    assert property.charge() == 8
    property.get_apartment()
    assert property.charge() == 12
    property2 = TypicalProperty("property2", 50, 400, "dark blue", 200)
    property2.get_apartment()
    assert property2.charge() == 400
    property2.get_apartment()
    assert property2.charge() == 600


def test_airport_charging():
    property = AirportProperty("property", 25, 100, "airport")
    player = Player("player")
    player.gain_property(property)
    assert property.charge() == 25
    property2 = AirportProperty("property2", 25, 100, "airport")
    player.gain_property(property2)
    assert property.charge() == 50
    assert property2.charge() == 50


def test_dice_charging():
    property = DiceChargeProperty("property", 10, 100, "dicecharge")
    player = Player("player")
    player.gain_property(property)
    assert property.charge(4) == 20
    property2 = DiceChargeProperty("property2", 10, 100, "dicecharge")
    player.gain_property(property2)
    assert property.charge(4) == 40
    assert property2.charge(4) == 40
