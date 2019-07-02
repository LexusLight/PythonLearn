# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designfin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from peewee import *
import sqlite3
db = SqliteDatabase('WorkersBase.db') #Переменная для хранения названия файла БД


class Workercode(Model): #Сооздаём таблицу наследуя от класса Peewee
    #code_id = CharField()
    job = CharField(unique=True)
    class Meta:
        database = db
    
class Worker(Model): #Сооздаём таблицу наследуя от класса Peewee
    name_f = CharField()
    name_i = CharField()
    name_o = CharField()
    number = IntegerField(unique=True)
    code_id = ForeignKeyField(Workercode, backref='codes')
    class Meta:
        database = db

def connectdb(): #Коннект к БД, при отсутствии таблиц инициализирует их
    db.connect()
    db.create_tables([Worker,Workercode])
   
class Ui_MainWindow(object):
    
    def loadData(self):#Загружаем через Sql запрос Данные в таблицу
        connection = sqlite3.connect("WorkersBase.db")
        query = "SELECT  worker.number, worker.name_f, worker.name_i, worker.name_o, workercode.job FROM worker INNER JOIN workercode ON worker.code_id = workercode.id"
        result = connection.execute(query)

        self.tableWidget.setRowCount(0)
        for row, row_data in enumerate(result):
            self.tableWidget.insertRow(row)
            for col, data in enumerate(row_data):
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(data)))
            self.checkParam()
        connection.close()
        
    def checkParam(self):
        global param
        param = 0
        for item in Worker.select():
            if item.number > param:
                param = item.number

        
    def increm(self): #инкрементация персонального номера относительно последней цифры
        self.checkParam()
        self.nameInput.setText(str(param+1))
        self.nameInput_4.setText("")
        self.nameInput_2.setText("")
        self.nameInput_3.setText("")

    def changingStart(self):
        for item in Worker.select():
            for item in Worker.select():
                self.nameInput.setText(str(item.number))
                self.nameInput_4.setText(item.name_f)
                self.nameInput_2.setText(item.name_i)
                self.nameInput_3.setText(item.name_o)
                self.combo.setCurrentIndex(int(str(item.code_id))-1)
   
    def getinfo(self): #Если Личный номер имеется в базе данных - вывводим все данные
        try:
            for item in Worker.select():
                if str(item.number) == str(self.nameInput.text()):
                    self.nameInput_4.setText(item.name_f)
                    self.nameInput_2.setText(item.name_i)
                    self.nameInput_3.setText(item.name_o)
                    self.combo.setCurrentIndex(int(str(item.code_id))-1)
                    return
                else:
                    self.nameInput_4.setText("")
                    self.nameInput_2.setText("")
                    self.nameInput_3.setText("")
                    self.combo.setCurrentIndex(0)
        except:
            print("Ошибка при загрузке из базы")

    def operation(self,button):#Проверка на нажатые радиобаттоны
        r1 = self.nameInput_4.text()
        r2 = self.nameInput_2.text()
        r3 = self.nameInput_3.text()
        if ((r1 == "") | (r2 == "") | (r3 == "")):
            return
        if self.add.isChecked():#Добавить айтем
            try:
                r1 = self.nameInput_4.text()
                r2 = self.nameInput_2.text()
                r3 = self.nameInput_3.text()
                r4 = int(self.nameInput.text())
                r5 = int(self.combo.currentIndex())+1
                guy1 = Worker.create(name_f = r1,
                                     name_i = r2,
                                     name_o = r3,
                                     number = r4,
                                     code_id = r5
                                     )
                self.increm()
            except:
                QtWidgets.QMessageBox.about(self,"Ошибка","Проверьте правильность ввода.")  
        elif self.change.isChecked():#Изменить айтем
                if str(item.number) == str(self.nameInput.text()):
                    item.name_f = self.nameInput_4.text()
                    item.name_i = self.nameInput_2.text()
                    item.name_o = self.nameInput_3.text()
                    item.code_id = int(self.combo.currentIndex())+1
                    item.save()
        elif self.delete_2.isChecked():#Удалить айтем  
            for item in Worker.select():
                if str(item.number) == str(self.nameInput.text()):
                    item.delete_instance()
                    item.save()
                    self.nameInput_4.setText("")
                    self.nameInput_2.setText("")
                    self.nameInput_3.setText("")
                    self.nameInput.setText("")
                    self.combo.setCurrentIndex(0)
        self.loadData()
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 351)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(140, 20, 111, 20))
        self.nameInput.setObjectName("nameInput")

        self.nameInput.textChanged[str].connect(self.getinfo)#

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(30, 90, 101, 31))
        self.btn.setObjectName("btn")     
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 641, 211))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Личный номер","Фамилия","Имя","Отчество","Профессия"])#
        self.tableWidget.setObjectName("tableWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 81, 16))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 101, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add = QtWidgets.QRadioButton(self.layoutWidget)
        self.add.setEnabled(True)
        self.add.setObjectName("add")
        self.add.setChecked(True)
        
        self.add.clicked.connect(self.increm)#
        
        self.verticalLayout.addWidget(self.add)
        self.change = QtWidgets.QRadioButton(self.layoutWidget)
        self.change.setObjectName("change")

        self.change.clicked.connect(self.changingStart)#
        
        self.verticalLayout.addWidget(self.change)
        self.delete_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.delete_2.setObjectName("delete_2")

        self.delete_2.clicked.connect(self.changingStart)#
        
        self.verticalLayout.addWidget(self.delete_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(380, 20, 291, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nameInput_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.nameInput_4.setObjectName("nameInput_4")
        self.verticalLayout_2.addWidget(self.nameInput_4)
        self.nameInput_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.nameInput_2.setObjectName("nameInput_2")
        self.verticalLayout_2.addWidget(self.nameInput_2)
        self.nameInput_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.nameInput_3.setObjectName("nameInput_3")
        self.verticalLayout_2.addWidget(self.nameInput_3)
        self.combo = QtWidgets.QComboBox(self.layoutWidget1)# Комбобокс
        for item in Workercode.select():
            self.combo.addItem(item.job)
        self.combo.setObjectName("combo")
        self.verticalLayout_2.addWidget(self.combo)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(270, 20, 82, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.nameInput.raise_()
        self.btn.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btn.clicked.connect(self.operation) #Проверка радиобаттанов
        self.increm()
        self.loadData() #Вставка базы

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сотрудники"))
        self.btn.setText(_translate("MainWindow", "Выполнить"))
        self.label.setText(_translate("MainWindow", "Личный номер"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.change.setText(_translate("MainWindow", "Изменить"))
        self.delete_2.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Фамилия"))
        self.label_3.setText(_translate("MainWindow", "Имя"))
        self.label_4.setText(_translate("MainWindow", "Отчество"))
        self.label_5.setText(_translate("MainWindow", "Должность"))
