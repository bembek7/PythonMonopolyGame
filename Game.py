from Player import Player
from Field import PropertyField
from Field import DiceChargePropertyField
from Dice import basic_roll


class Game:
    def __init__(self, board) -> None:
        self.board = board
        self.players = []

    def roll_dice_result(self):
        self._dice_result = basic_roll(2, 6)
        self._dice_result = 1
        return self._dice_result

    def field_action(self, pos, player):
        if isinstance(self.board[pos], DiceChargePropertyField):
            self.board[pos].Action(player, self._dice_result)
        else:
            self.board[pos].Action(player)

    def get_board_length(self):
        return self.get_board_length

    def add_player(self, name):
        self.players.append(Player(name))

    def sell_property(self, seller, price, propertyname, buyer_name):
        for player in self.players:
            if player.get_name() == buyer_name:
                buyer = player
                break
        for field in self.board:
            if isinstance(field, PropertyField):
                if field.get_property().get_name() == propertyname:
                    property = field.get_property()
                    break
        seller.lose_property(property)
        seller.gain(price)
        buyer.gain_property(property)
        buyer.pay(price)
