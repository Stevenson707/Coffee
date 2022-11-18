import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow

DB_NAME = 'coffee.sqlite'


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect(DB_NAME)
        self.showw()

    def showw(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName(DB_NAME)
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = self.tableView
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('Espresso')
        model.select()
        self.model = model

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())