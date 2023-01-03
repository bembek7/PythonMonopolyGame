from PySide2.QtWidgets import QMainWindow
from Dice import basic_roll
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore
from Property import TypicalProperty
from ui_GameWindow import Ui_MainWindow
from Field import PropertyField


class MainWindow(QMainWindow):
    def __init__(self, game, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.plansze.setCurrentIndex(0)
        self.ui.DodajGraczaButton.clicked.connect(self.add_player)
        self.ui.GrajButton.clicked.connect(self.clicked_play)
        self.ui.RzutButton.clicked.connect(self.rolled)
        self.ui.KoniecTuryButton.clicked.connect(self.end_turn)
        self.ui.KupButton.clicked.connect(self.player_buys)
        self.ui.ZastawButton.clicked.connect(self.deactivating_property)
        self.ui.WykupButton.clicked.connect(self.activating_property)
        self.ui.KupDomekButton.clicked.connect(self.buying_apartment)
        self.ui.SprzedajDomekButton.clicked.connect(self.selling_apartment)
        self.ui.ZastawButton.setEnabled(False)
        self.ui.GrajButton.setEnabled(False)
        self._used_names = []
        self._game_instance = game
        self._board = self._game_instance.board
        self._curr_player_index = 0
        self.ui.ListaGraczyGra.itemClicked.connect(self.show_player)
        self.already_rolled = False
        self.set_names()
        self.set_prices()
        self.set_properties()

    def selling_apartment(self):
        if self.ui.ListaSprzedania.currentItem() is not None:
            property_name = self.ui.ListaSprzedania.currentItem().text()
            for field in self._board:
                if isinstance(field, PropertyField):
                    property = field.get_property()
                    if isinstance(property, TypicalProperty):
                        if property.get_name() == property_name:
                            self._curr_player.sell_apartment(property)
                            break
            self.update_lists()

    def buying_apartment(self):
        if self.ui.ListaKupienia.currentItem() is not None:
            property_name = self.ui.ListaKupienia.currentItem().text()
            for field in self._board:
                if isinstance(field, PropertyField):
                    property = field.get_property()
                    if isinstance(property, TypicalProperty):
                        if property.get_name() == property_name:
                            self._curr_player.buy_apartment(property)
                            break
            self.update_lists()

    def deactivating_property(self):
        pass

    def activating_property(self):
        pass

    def show_list_widget(self, list_widget, properties, button):
        list_widget.clear()
        for property in properties:
            list_widget.addItem(property.get_name())
        button.setEnabled(len(properties) > 0)

    def update_lists(self):
        self.show_deactivable_properties()
        self.show_activable_properties()
        self.show_available_apartments()
        self.show_sellable_apartments()
        self.set_properties()
        self.show_player(self.ui.ListaGraczyGra.currentItem())
        if self.already_rolled:
            self.ui.KupDomekButton.setEnabled(False)

    def show_sellable_apartments(self):
        self.show_list_widget(self.ui.ListaSprzedania, self._curr_player.get_sellable_apartments(), self.ui.SprzedajDomekButton)

    def show_available_apartments(self):
        self.show_list_widget(self.ui.ListaKupienia, self._curr_player.get_available_apartments(), self.ui.KupDomekButton)

    def show_deactivable_properties(self):
        self.show_list_widget(self.ui.ListaWykup, self._curr_player.get_deactivable_properties(), self.ui.WykupButton)

    def show_activable_properties(self):
        self.show_list_widget(self.ui.LisatZastaw, self._curr_player.get_activable_properties(), self.ui.ZastawButton)

    # def deactivate_property(self):
    #     if self.ui.ListaGraczyGra.currentItem() is not None:
    #         if self.ui.ListaGraczyGra.currentItem().text() == self._curr_player.get_name():
    #             if self.ui.ListaPosiadlosci.currentItem() is not None:
    #                 property_name = self.ui.ListaPosiadlosci.currentItem().text()
    #                 self._curr_player.deactivate_property(property_name)

    def show_player(self, item):
        if item is not None:
            for player in self._game_instance.players:
                if player.get_name() == item.text():
                    self.ui.Pieniadze.setText(str(player.get_cash()))
                    self.ui.ListaPosiadlosci.clear()
                    for property in player.get_properties():
                        self.ui.ListaPosiadlosci.addItem(str(property))
                    break

    def set_properties(self):
        for a in range(0, 40):
            if isinstance(self._board[a], PropertyField):
                property = self._board[a].get_property()
                if isinstance(property, TypicalProperty):
                    if not property.is_active():
                        string = "Zastawione"
                    elif property.get_apartments_nr() < 5:
                        string = f"Liczba domków : {property.get_apartments_nr()}"
                    else:
                        string = "Hotel"
                    if a <= 9:
                        self.ui.gridLayout_2.itemAtPosition(0, a).itemAt(2).widget().setText(string)
                    elif a <= 19:
                        self.ui.gridLayout_2.itemAtPosition(a-10, 10).itemAt(2).widget().setText(string)
                    elif a <= 29:
                        self.ui.gridLayout_2.itemAtPosition(10, abs(a-30)).itemAt(2).widget().setText(string)
                    else:
                        self.ui.gridLayout_2.itemAtPosition(abs(a-40), 0).itemAt(2).widget().setText(string)

    def set_prices(self):
        for a in range(0, 40):
            if isinstance(self._board[a], PropertyField):
                property = self._board[a].get_property()
                if a <= 9:
                    self.ui.gridLayout_2.itemAtPosition(0, a).itemAt(4).widget().setText(str(property.get_price()))
                elif a <= 19:
                    self.ui.gridLayout_2.itemAtPosition(a-10, 10).itemAt(4).widget().setText(str(property.get_price()))
                elif a <= 29:
                    self.ui.gridLayout_2.itemAtPosition(10, abs(a-30)).itemAt(4).widget().setText(str(property.get_price()))
                else:
                    self.ui.gridLayout_2.itemAtPosition(abs(a-40), 0).itemAt(4).widget().setText(str(property.get_price()))

    def set_names(self):
        for a in range(0, 40):
            if a <= 9:
                self.ui.gridLayout_2.itemAtPosition(0, a).itemAt(0).widget().setText(self._board[a].get_name())
            elif a <= 19:
                self.ui.gridLayout_2.itemAtPosition(a-10, 10).itemAt(0).widget().setText(self._board[a].get_name())
            elif a <= 29:
                self.ui.gridLayout_2.itemAtPosition(10, abs(a-30)).itemAt(0).widget().setText(self._board[a].get_name())
            else:
                self.ui.gridLayout_2.itemAtPosition(abs(a-40), 0).itemAt(0).widget().setText(self._board[a].get_name())

    def clicked_play(self):
        self.ui.plansze.setCurrentIndex(1)
        self.turn()
        for player in self._game_instance.players:
            index = 3
            self.ui.gridLayout_2.itemAtPosition(0, 0).itemAt(index).widget().addItem(player.get_name())

    def player_buys(self):
        self._board[self._curr_player.get_position()].buy(self._curr_player)
        self.ui.KupButton.setEnabled(False)
        self.update_lists()

    def _setupPlayersList(self, name):
        self.ui.ListaGraczy.addItem(name)
        self.ui.ListaGraczyGra.addItem(name)

    def roll_dice_result(self):
        result = basic_roll(2, 6)
        self.ui.WynikRzutu.setText(f"Wynik rzutu {result}")
        return result

    def rolled(self):
        # result = self.roll_dice_result()
        self.already_rolled = True
        result = 1
        self.ui.KupDomekButton.setEnabled(False)
        self.ui.RzutButton.setEnabled(False)
        old_pos = self._curr_player.get_position()
        self._curr_player.move(result)
        new_pos = self._curr_player.get_position()
        self.update_player_pos(old_pos, new_pos)
        self.perform_field_action(new_pos)
        self.update_lists()

    def check_buying(self):
        if self._board[self._curr_player.get_position()].can_buy(self._curr_player):
            self.ui.KupButton.setEnabled(True)

    def perform_field_action(self, pos):
        self._board[pos].Action(self._curr_player)
        # if pos == 30:
        #     self.go_to_jail()
        self.check_buying()
        self.ui.KoniecTuryButton.setEnabled(True)

    def go_to_jail(self):
        old_pos = self._curr_player.get_position()
        self._curr_player.move(20)
        new_pos = self._curr_player.get_position()
        self.update_player_pos(old_pos, new_pos)
        self._curr_player.pay(200)
    ###

# 0-9 0,pos | 10-19 pos-10,10 | 20-29 10,abs(pos-30) | 30-39  abs(pos-40),0
    def update_player_pos(self, old_pos, new_pos):
        index = 3
        if old_pos <= 9:
            self.deleteItem(self._curr_player.get_name(), self.ui.gridLayout_2.itemAtPosition(0, old_pos).itemAt(index).widget())
        elif old_pos <= 19:
            self.deleteItem(self._curr_player.get_name(), self.ui.gridLayout_2.itemAtPosition(old_pos-10, 10).itemAt(index).widget())
        elif old_pos <= 29:
            self.deleteItem(self._curr_player.get_name(), self.ui.gridLayout_2.itemAtPosition(10, abs(old_pos-30)).itemAt(index).widget())
        else:
            self.deleteItem(self._curr_player.get_name(), self.ui.gridLayout_2.itemAtPosition(abs(old_pos-40), 0).itemAt(index).widget())
        if new_pos <= 9:
            self.ui.gridLayout_2.itemAtPosition(0, new_pos).itemAt(index).widget().addItem(self._curr_player.get_name())
        elif new_pos <= 19:
            self.ui.gridLayout_2.itemAtPosition(new_pos-10, 10).itemAt(index).widget().addItem(self._curr_player.get_name())
        elif new_pos <= 29:
            self.ui.gridLayout_2.itemAtPosition(10, abs(new_pos-30)).itemAt(index).widget().addItem(self._curr_player.get_name())
        else:
            self.ui.gridLayout_2.itemAtPosition(abs(new_pos-40), 0).itemAt(index).widget().addItem(self._curr_player.get_name())

    def add_player(self):
        if self.ui.ListaGraczy.count() < 6 and self.ui.lineEdit.text().strip() != "" and self.ui.lineEdit.text() not in self._used_names:
            self._setupPlayersList(self.ui.lineEdit.text())
            self._used_names.append(self.ui.lineEdit.text())
            self._game_instance.add_player(self.ui.lineEdit.text())
        self.ui.lineEdit.setText("")
        if len(self._used_names) >= 2:
            self.ui.GrajButton.setEnabled(True)

    def turn(self):
        self._curr_player = self._game_instance.players[self._curr_player_index]
        self.ui.Tura.setText(f"Tura gracza : {self._curr_player.get_name()}")
        self.ui.KoniecTuryButton.setEnabled(False)
        self.ui.KupButton.setEnabled(False)
        self.ui.RzutButton.setEnabled(True)
        self.update_lists()

    #########

    def deleteItem(self, itemName, list):
        items_list = list.findItems(itemName, QtCore.Qt.MatchExactly)
        for item in items_list:
            list.takeItem(list.row(item))

    def end_turn(self):
        self._curr_player_index = (self._curr_player_index + 1) % len(self._used_names)
        self.already_rolled = False
        self.turn()


def gui_main(game, args):
    app = QApplication(args)
    window = MainWindow(game)

    window.showMaximized()
    return app.exec_()
