from Player import Player
from Property import TypicalProperty


def test_init():
    player = Player("new_player")
    assert player.get_name() == "new_player"
    assert player.get_cash() == 1500
    assert player.get_position() == 0


def test_money():
    player = Player("new_player")
    player.pay(500)
    assert player.get_cash() == 1000
    player.gain(125)
    assert player.get_cash() == 1125
    assert player.can_afford(1300) is False
    assert player.can_afford(1000) is True


def test_jail():
    player = Player("new_player")
    player.imprison()
    assert player.get_rounds_left() == 3
    assert player.is_in_jail() is True
    player.decrement_rounds()
    assert player.get_rounds_left() == 2
    player.free()
    assert player.is_in_jail() is False


def test_moving():
    player = Player("new_player")
    assert player.get_position() == 0
    player.move(5)
    assert player.get_position() == 5
    player.imprison()
    player.move(3)
    assert player.get_position() == 5


def test_moving_through_start():
    player = Player("player")
    player.set_position(38)
    assert player.get_position() == 38
    assert player.get_cash() == 1500
    player.move(3)
    assert player.get_position() == 1
    assert player.get_cash() == 1700


def test_properties():
    player = Player("player")
    assert player.get_properties() == []
    property = TypicalProperty("1", 1, 1, "brown", 2)
    player.gain_property(property)
    assert player.get_properties() == [property]
    player.lose_property(property)
    assert player.get_properties() == []
    player.gain_property(property)
    assert player.get_sellable_properties() == [property]
    assert player.get_activable_properties() == []
    assert player.get_deactivable_properties() == [property]
    player.buy_apartment(property)
    assert player.get_cash() == 1498
    assert player.get_sellable_properties() == []
    assert player.get_deactivable_properties() == []
    assert player.get_available_apartments() == []
    player.sell_apartment(property)
    assert player.get_cash() == 1499
    property2 = TypicalProperty("2", 1, 1, "brown", 2)
    player.gain_property(property2)
    assert player.can_apartment_property("brown", 0) is True
    assert player.can_apartment_property("brown", 1) is False
    assert player.check_other_apartments(property) is True
    player.buy_apartment(property2)
    assert player.get_cash() == 1497
    assert player.check_other_apartments(property) is False


def test_apartments():
    player = Player("player")
    property = TypicalProperty("1", 1, 1, "brown", 2)
    property2 = TypicalProperty("2", 1, 1, "brown", 2)
    player.buy_property(property)
    assert player.get_cash() == 1499
    assert player.can_buy_apartment() is False
    player.buy_property(property2)
    assert player.get_cash() == 1498
    assert player.can_buy_apartment() is True
    assert player.get_available_apartments() == [property, property2]
    player.buy_apartment(property2)
    assert player.get_available_apartments() == [property]
    player.sell_apartment(property2)
    assert player.get_available_apartments() == [property, property2]
    player.deactivate_property(property)
    assert player.get_available_apartments() == []


def test_losing():
    player = Player("player")
    property = TypicalProperty("1", 1, 1, "brown", 2)
    player.buy_property(property)
    player.buy_apartment(property)
    assert property.get_apartments_nr() == 1
    player.lose()
    assert property.get_apartments_nr() == 0
