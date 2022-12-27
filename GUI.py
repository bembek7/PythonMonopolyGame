from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget, QMainWindow, QListWidgetItem

import sys

from ui_GameWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.DodajGraczaButton.clicked.connect(self.AddPlayer)
        self.ui.GrajButton.clicked.connect(self.ClickedPlay)
        self.UsedNames = []
    
    def ClickedPlay(self):
        self.ui.plansze.setCurrentIndex(1)

    def _setupPlayersList(self, name):
        self.ui.ListaGraczy.addItem(name)
    
    def AddPlayer(self):
        if self.ui.ListaGraczy.count() < 6 and self.ui.lineEdit.text().strip() != "" and self.ui.lineEdit.text() not in self.UsedNames:
            self._setupPlayersList(self.ui.lineEdit.text())
            self.UsedNames.append(self.ui.lineEdit.text())

def guiMain(args):
    app = QApplication(args)
    window = MainWindow()

    window.show()
    return app.exec_()

if __name__ == "__main__":
    guiMain(sys.argv)