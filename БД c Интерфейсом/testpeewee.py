from peewee import *
from module1 import *
from PyQt5 import QtWidgets
import design
import sys
print('Подключение')

class ExampleApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
    if __name__ != '__main__':
        main()
design.connectdb()
main()
#Inp.Create()
