# pieniądze
# lista posiadlosci
class Player:
    def __init__(self, name) -> None:
        self._name = name
        self._cash = 1500
        self._position = 0
        self._owning = []
    
    def get_name(self):
        return self._name

    def pay_cash(self, amount):
        if self._cash - amount >= 0:
            self._cash = self._cash - amount
    # wymuszenie zastawu/sprzedaży

    def move(self, result):
        board_places = 40
        if self._position + result < 0:
            self._position = board_places + self._position + result
        self._position = (self._position + result) % board_places