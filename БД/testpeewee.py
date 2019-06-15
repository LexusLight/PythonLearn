from peewee import *
#from playhouse.sqlite_ext import SqliteExtDatabase
print('Пытаемся подключиться')

#db = SqliteExtDatabase('Hardware.db',regexp_function = True,timeout = 3,pragmas = {'journal_mode':'wal'})
#db.connect()
db = SqliteDatabase('Hardware2.db')

class Hardware2(Model): #Peewee автоматически выведет имя таблицы базы данных из имени класса
    name_hw = CharField() #Так мы создаём главную таблицу
    about_hw = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Hardware2])

def CreateFields():
    item1 = Hardware2(name_hw = "Intel Atom", about_hw = "какое то описание фыфыаф")
    item2 = Hardware2(name_hw = "Intel Core", about_hw = "штеул лучший процессор")
    item3 = Hardware2(name_hw = "Intel Core 2", about_hw = "Сам сижду и всем советую")
    item1.save()
    item2.save()
    item3.save()

def info(x):
    ask = Hardware2.get(Hardware2.name_hw == x)
    print(ask)
    print(ask.about_hw)
    
def listinfo():
    for item in Hardware2.select():
        print(item.name_hw)
