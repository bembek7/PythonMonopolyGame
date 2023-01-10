from random import randint
from Player import Player
from Field import PropertyField
from Field import DiceChargePropertyField
from Field import ChanceField
from Dice import basic_roll


class Game:
    """
    A class for storing useful methods in game.

    ...

    Attributes
    ----------
    board : list
        a list of fields that make up the game board
    players : list
        a list of players that are playing the game
    chance_result : int
        a variable that holds the current result of a chance card
    jail_price : int
        the cost to leave jail

    Methods
    -------
    who_wins():
        returns the player with most cash
    free_player(player:Player)
        player pay jail_price and freed from jail
    get_activation_price_from_name(name:str)
        gets the activation price from property from its name
    get_apartment_price_from_name(name:str)
        gets the apartment price from property from its name
    field_action(pos:int, player:Player):
        depending on the field player is on, performs the action
    player_loses(player:Player):
        removes player from game and set his all properties to not have owner
    add_player(name:str)
        adds player to the game with the given name
    sell_property(seller:Player, price:int, propertyname:str, buyer_name:str)
        transfer the property from seller to buyer for the price.
    """
    def __init__(self, board) -> None:
        self.board = board
        self.players = []
        self._chance_result = 0
        self._jail_price = 50

    def who_wins(self):
        max_cash = 0
        winner_name = ""
        for player in self.players:
            if player.get_cash() > max_cash:
                winner_name = player.get_name()
                max_cash = player.get_cash()
        return winner_name

    def free_player(self, player):
        player.pay(self._jail_price)
        player.free()

    def get_jail_price(self):
        return self._jail_price

    def get_activation_price_from_name(self, name):
        for field in self.board:
            if field.get_name() == name:
                return field.get_property().get_price() / 2 + field.get_property().get_price() / 10
                break

    def get_apartment_price_from_name(self, name):
        for field in self.board:
            if field.get_name() == name:
                return field.get_property().get_apartment_price()
                break

    def zero_chance_result(self):
        self._chance_result = 0

    def get_chance_result(self):
        return self._chance_result

    def roll_dice_result(self):
        self._dice_result = basic_roll(2, 6)
        self._dice_result = 15  # changing for test reasons
        return self._dice_result

    def field_action(self, pos, player):
        if isinstance(self.board[pos], ChanceField):
            self._chance_result = randint(-50, 50)
            if self._chance_result == 0:
                self._chance_result += 1
            self.board[pos].action(player, self._chance_result)
        else:
            self._chance_result == 0
            if isinstance(self.board[pos], DiceChargePropertyField):
                self.board[pos].action(player, self._dice_result)
            else:
                self.board[pos].action(player)

    def player_loses(self, player):
        self.players.remove(player)
        player.lose()

    def get_board_length(self):
        return len(self.board)

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
