#!/usr/bin/python3
import json

from ui import passwordmanager_ui as ui

class Passwordmanager:
    def __init__(self):
        self.action = 0
    
    def read_menu_action(self):
        return int(input("Was möchten sie tun? "))

    def switch_action(self):
        match self.action:
            case 1:
                self.write_file()
                #self.create_new_database()
            case 2:
                self.use_existing_database()
            case 3:
                exit()

    def create_new_database(self):
        pass

    def fake_db(self):
        return [
            {
            "name": "leon",
            "password": "123",
            "url": "www.123.de",
            "note": ""
            },
            {
            "name": "hannes",
            "password": "321",
            "url": "www.321.de",
            "note": "hannes"
            }
        ]

    def write_file(self):
        #json_dump = 

        with open("testdb.json", "w") as outfile:
            outfile.write(json.dumps(self.fake_db(), indent=2))

    def use_existing_database(self):
        pass

    def run(self):
        while True:
            ui.show_menu()
            self.action = self.read_menu_action()
            print("")
            self.switch_action()

passwordmanager = Passwordmanager()
passwordmanager.run()