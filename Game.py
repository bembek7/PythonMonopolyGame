from Player import Player


class Game:
    def __init__(self, board) -> None:
        self.board = board
        self.players = []

    def get_board_length(self):
        return self.get_board_length

    def add_player(self, name):
        self.players.append(Player(name))

    def sell_property(self, seller, price, propertyname, buyer):
        for field in self.board:
            if field.get_property().get_name() == propertyname:
                property = field.get_property()
                break
        seller.lose_property(property)
        seller.gain(price)
        buyer.gain_property(property)
        buyer.pay(price)
