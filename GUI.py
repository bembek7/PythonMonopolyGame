import time
from PySide2.QtWidgets import QWidget, QMainWindow, QListWidgetItem, QListView
from Dice import basic_roll
from PySide2.QtWidgets import QApplication
from Game import Game
from PySide2 import QtCore
from ui_GameWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, game, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.plansze.setCurrentIndex(0)
        self.ui.DodajGraczaButton.clicked.connect(self.add_player)
        self.ui.GrajButton.clicked.connect(self.clicked_play)
        self.ui.RzutButton.clicked.connect(self.rolled)
        self._used_names = []
        self._game_instance = game
        self._curr_player_index = 0
    
    def clicked_play(self):
        self.ui.plansze.setCurrentIndex(1)
        self.turn()
        for player in self._game_instance.players:
            index = 3
            self.ui.gridLayout_2.itemAtPosition(0,0).itemAt(index).widget().addItem(player.get_name())


    def _setupPlayersList(self, name):
        self.ui.ListaGraczy.addItem(name)

    def roll_dice_result(self):
        result = basic_roll(2,6)
        self.ui.WynikRzutu.setText(str(result))
        return result

    def rolled(self):
        result = self.roll_dice_result()
        self.ui.KupDomekButton.setEnabled(False)
        self.ui.RzutButton.setEnabled(False)
        old_pos = self._game_instance.players[self._curr_player_index].get_position()
        self._game_instance.players[self._curr_player_index].move(result)
        new_pos = self._game_instance.players[self._curr_player_index].get_position()
        self.update_player_pos(old_pos, new_pos)
        self.perform_field_action(new_pos)

    def perform_field_action(self, pos)
        pass
    ###

# 0-9 0,pos | 10-19 pos-10,10 | 20-29 10,abs(pos-30) | 30-39  abs(pos-40),0
    def update_player_pos(self, old_pos, new_pos):
        player = self._game_instance.players[self._curr_player_index]
        index = 3
        if old_pos <= 9:
            self.deleteItem(player.get_name(), self.ui.gridLayout_2.itemAtPosition(0,old_pos).itemAt(index).widget())
        elif old_pos <= 19:
            self.deleteItem(player.get_name(), self.ui.gridLayout_2.itemAtPosition(old_pos-10,10).itemAt(index).widget())
        elif old_pos <= 29:
            self.deleteItem(player.get_name(), self.ui.gridLayout_2.itemAtPosition(10,abs(old_pos-30)).itemAt(index).widget())
        else:
            self.deleteItem(player.get_name(), self.ui.gridLayout_2.itemAtPosition(abs(old_pos-40),0).itemAt(index).widget())
        if new_pos <= 9:
            self.ui.gridLayout_2.itemAtPosition(0,new_pos).itemAt(index).widget().addItem(player.get_name())
        elif new_pos <= 19:
            self.ui.gridLayout_2.itemAtPosition(new_pos-10,10).itemAt(index).widget().addItem(player.get_name())
        elif new_pos <= 29:
            self.ui.gridLayout_2.itemAtPosition(10,abs(new_pos-30)).itemAt(index).widget().addItem(player.get_name())
        else:
            self.ui.gridLayout_2.itemAtPosition(abs(new_pos-40),0).itemAt(index).widget().addItem(player.get_name())

    def add_player(self):
        if self.ui.ListaGraczy.count() < 6 and self.ui.lineEdit.text().strip() != "" and self.ui.lineEdit.text() not in self._used_names:
            self._setupPlayersList(self.ui.lineEdit.text())
            self._used_names.append(self.ui.lineEdit.text())
            self._game_instance.add_player(self.ui.lineEdit.text())
        self.ui.lineEdit.setText("")

    def turn(self):
        self.ui.Tura.setText(f"Tura gracza : {self._used_names[self._curr_player_index]}")
    ######### 

    def deleteItem(self, itemName, list):
        items_list = list.findItems(itemName, QtCore.Qt.MatchExactly)
        for item in items_list:
                delete = list.row(item)
                list.takeItem(delete)

def gui_main( game, args):
    app = QApplication(args)
    window = MainWindow(game)

    window.show()
    return app.exec_()