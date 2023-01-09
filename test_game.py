from Game import Game
from Field import PropertyField
from Property import TypicalProperty


def test_init():
    game = Game([])
    assert game.get_jail_price() == 50
    assert game.get_chance_result() == 0
    assert game.get_board_length() == 0


def test_winning():
    game = Game([])
    game.add_player("a")
    game.add_player("b")
    game.players[0].pay(50)
    assert game.who_wins() == "b"


def test_losing():
    game = Game([])
    game.add_player("a")
    game.add_player("b")
    game.player_loses(game.players[0])
    assert len(game.players) == 1
    assert game.players[0].get_name() == "b"


def test_selling():
    property = TypicalProperty("Brown1", 2, 60, "brown", 50)
    board = [PropertyField(1, property)]
    game = Game(board)
    game.add_player("a")
    game.add_player("b")
    game.players[0].buy_property(property)
    game.sell_property(game.players[0], 200, "Brown1", "b")
    assert game.players[0].get_cash() == 1640
    assert game.players[1].get_cash() == 1300
    assert game.players[1].get_properties() == [property]
