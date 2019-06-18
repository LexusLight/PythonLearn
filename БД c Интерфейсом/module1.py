from peewee import *

db = SqliteDatabase('Hardware.db')

class Hardware(Model):
    name_hw = CharField()
    about_hw = CharField()
    class Meta:
        database = db
        
class Inp():
    def Create():
        db.connect()
        db.create_tables([Hardware])
    def Ask():
        print()
        string1 = input("Действие(Добавить, Показать, Изменить, Удалить): ")
        
        if (string1.lower() == "добавить"):
            Inp.Add()
        elif (string1.lower() == "показать"):
            Inp.Select()
        elif (string1.lower() == "изменить"):
            Inp.Change()
        elif (string1.lower() == "удалить"):
            Inp.Delete()
        else:
            print("Неправильно введена команда")
            return Inp.Ask()
    def Add():
        string1 = input("Введите данные через запятую(Объект, описание): ")
        string1 = string1.split(",")
        field1 = Hardware(name_hw = string1[0],about_hw = string1[1])
        field1.save()
        print("Добавлено.")
        Inp.Ask()
    def Select():
        i = 1;
        for item in Hardware.select():
            print(str(i)+":"+item.name_hw +" - "+ item.about_hw)
            i+=1
        Inp.Ask()
    def Change():
        string1 = input("Введите название Объекта: ")
        string2 = input("Введите изменение: ")
        for item in Hardware.select():
            if item.name_hw == string1:
                item.about_hw = string2
                item.save()
                print("Изменение принято.")
        Inp.Ask()
    def Delete():
        string1 = input("Введите название Объекта: ")
        for item in Hardware.select():
            if item.name_hw == string1:
                item.delete_instance()
                print("Удалено.")
        Inp.Ask()
        
