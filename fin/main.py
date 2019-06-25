from peewee import *
from PyQt5 import QtWidgets
import designfin
import sys
print('Подключение')

class ExampleApp(QtWidgets.QMainWindow,designfin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
    window.loadData()
    if __name__ != '__main__':
        main()
designfin.connectdb()
main()
#Inp.Create()
