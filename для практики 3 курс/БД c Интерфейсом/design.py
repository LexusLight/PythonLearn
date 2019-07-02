# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from peewee import *
import sqlite3
db = SqliteDatabase('Hardware.db')

class Hardware(Model):
    name_hw = CharField()
    about_hw = CharField()
    class Meta:
        database = db
class connectdb():
    db.connect()
    db.create_tables([Hardware])
    db.close()
class Ui_MainWindow(object):
    def loadData(self):
        connection = sqlite3.connect("Hardware.db")
        query = "SELECT * FROM hardware"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row, row_data in enumerate(result):
            self.tableWidget.insertRow(row)
            for col, data in enumerate(row_data):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(data)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 278)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(370, 70, 111, 20))
        self.nameInput.setObjectName("nameInput")
        self.add = QtWidgets.QRadioButton(self.centralwidget)
        self.add.setEnabled(True)
        self.add.setGeometry(QtCore.QRect(370, 10, 82, 17))
        self.add.setObjectName("add")
        self.change = QtWidgets.QRadioButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(370, 30, 82, 17))
        self.change.setObjectName("change")
        self.delete_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(370, 50, 82, 17))
        self.delete_2.setObjectName("delete_2")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(370, 230, 75, 23))
        self.btn.setObjectName("btn")

        self.btn.clicked.connect(self.loadData)
        
        self.textInput = QtWidgets.QTextEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(370, 100, 111, 121))
        self.textInput.setObjectName("textInput")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 351, 241))
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.change.setText(_translate("MainWindow", "Изменить"))
        self.delete_2.setText(_translate("MainWindow", "Удалить"))
        self.btn.setText(_translate("MainWindow", "Выполнить"))

