# pieniądze
# lista posiadlosci
class Player:
    def __init__(self, name) -> None:
        self._name = name
        self._cash = 1500
        self._position = 0
        self._properties = []
        self._in_jail = False
    
    def get_name(self):
        return self._name

    def pay(self, amount):
        if self._cash - amount >= 0:
            self._cash = self._cash - amount
        return True
    # wymuszenie zastawu/sprzedaży

    def get_amount_of_type(self, type):
        result = 0
        for property in self._properties:
            if property.get_type() == type:
                result += 1
        return result

    def buy_property(self, property):
        self._properties.append(property)

    def move(self, result, game):
        board_places = 40
        if self._position + result < 0:
            self._position = board_places + self._position + result
        self._position = (self._position + result) % board_places