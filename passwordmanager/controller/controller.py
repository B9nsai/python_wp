import sys
import json 

sys.path.append('../model')
from model import fake_db
from view import passwordmanager_ui as ui





class Controller:
    def __init__(self):
        self.__startup_menu = self.Startup_menu(self)
        self.__db_menu = self.DB_menu(self)

    def run(self):
        self.__startup_menu.run()

    def create_new_database(self):
        self.__db_menu.create_new_database()

    def use_existing_database(self):
        self.__db_menu.use_existing_database()

    def set_db_name(self, db_name):
        self.__db_name = db_name

    def get_db_name(self):
        return self.__db_name



    class Startup_menu:
        def __init__(self, outer):
            self.__action = 0
            self.__outer = outer

        def run(self):
            ui.show_startup_menu()
            self.__read_startup_menu_action()
            print()
            self.__switch_action()
            print()

        def __read_startup_menu_action(self):
            self.__action = int(input("Was möchten sie tun? "))

        def __switch_action(self):
            match self.__action:
                case 0:
                    #dev tests
                    self.write_file()
                case 1:
                    self.__outer.create_new_database()
                case 2:
                    self.__outer.use_existing_database()
                case 3:
                    exit() 
     
    class DB_menu:
        def __init__(self, outer):
            self.__action = 0
            self.__outer = outer 


        def switch_db_menu_action(self):
            match self.__action:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass

        def create_new_database(self):
            self.__outer.set_db_name(input("Bitte geben sie den Namen der Datenbank ein: "))
            ui.show_db_menu(self.__outer.get_db_name())

        def use_existing_database(self):
            pass

        def write_file(self):
            self.fake_db = fake_db.fake_db()
            with open("testdb.json", "w") as outfile:
                outfile.write(json.dumps(self.fake_db.get_db(), indent=2))

        def use_existing_database(self):
            pass
    