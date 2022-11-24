import sys
import json 

sys.path.append('../model')
from model import fake_db

class controller:
    def __init__(self):
        self.action = 0

    def read_startup_menu_action(self):
        return int(input("Was möchten sie tun? "))

    def switch_startup_menu_action(self):
        match self.action:
            case 0:
                #tests
                self.write_file()
            case 1:
                self.create_new_database()
            case 2:
                self.use_existing_database()
            case 3:
                exit()  

    def switch_db_menu_action(self):
        match self.db_action:
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
        self.db_name = input("Bitte geben sie den Namen der Datenbank ein: ")
        self.show_db_menu()
        pass

    def use_existing_database(self):
        pass

    def write_file(self):
        self.fake_db = fake_db.fake_db()
        with open("testdb.json", "w") as outfile:
            outfile.write(json.dumps(self.fake_db.get_db(), indent=2))

    def use_existing_database(self):
        pass