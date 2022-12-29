import time
from PySide2.QtWidgets import QWidget, QMainWindow, QListWidgetItem
from Dice import basic_roll
from PySide2.QtWidgets import QApplication
from Game import Game

from ui_GameWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, game, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.plansze.setCurrentIndex(0)
        self.ui.DodajGraczaButton.clicked.connect(self.add_player)
        self.ui.GrajButton.clicked.connect(self.clicked_play)
        self.ui.RzutButton.clicked.connect(self.roll_dice_result)
        self._used_names = []
        self._game_instance = game
    
    def clicked_play(self):
        self.ui.plansze.setCurrentIndex(1)
        self.play()

    def _setupPlayersList(self, name):
        self.ui.ListaGraczy.addItem(name)

    def roll_dice_result(self):
        result = basic_roll(2,6)
        self.ui.WynikRzutu.setText(str(result))
        return result

    def add_player(self):
        if self.ui.ListaGraczy.count() < 6 and self.ui.lineEdit.text().strip() != "" and self.ui.lineEdit.text() not in self._used_names:
            self._setupPlayersList(self.ui.lineEdit.text())
            self._used_names.append(self.ui.lineEdit.text())
            self._game_instance.add_player(self.ui.lineEdit.text())
        self.ui.lineEdit.setText("")

    def play(self):
        for name in self._used_names:
            self.ui.Tura.setText(f"Tura gracza : {name}")
    #########

def gui_main( game, args):
    app = QApplication(args)
    window = MainWindow(game)

    window.show()
    return app.exec_()