from random import randint
from Player import Player
from Field import PropertyField
from Field import DiceChargePropertyField
from Field import ChanceField
from Dice import basic_roll


class Game:
    def __init__(self, board) -> None:
        self.board = board
        self.players = []
        self._chance_result = 0

    def get_chance_result(self):
        return self._chance_result

    def roll_dice_result(self):
        self._dice_result = basic_roll(2, 6)
        self._dice_result = 5  # ########################################
        return self._dice_result

    def field_action(self, pos, player):
        if isinstance(self.board[pos], ChanceField):
            self._chance_result = randint(-50, 50)
            if self._chance_result == 0:
                self._chance_result += 1
            self.board[pos].Action(player, self._chance_result)
        else:
            self._chance_result == 0
            if isinstance(self.board[pos], DiceChargePropertyField):
                self.board[pos].Action(player, self._dice_result)
            else:
                self.board[pos].Action(player)

    def player_loses(self, player):
        self.players.remove(player)
        player.lose()

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
