#!/usr/bin/python3

import json

import database
class passwordmanager:
        
    def __init__(self):
        self.__db = database.database()

    def main(self):
        while(True):
            db = database.database()
            self.run_startup_menu()

    def run_startup_menu(self):
        self.show_startup_menu()
        self.match_startup_menu_option()

    def show_startup_menu(self):
        print("\n=============================================")
        print("               Passwordmanager               ")
        print("=============================================")
        print("  1) Neue Passwortdatenbank erstellen        ")
        print("  2) Existierende Passwortdatenbank verwenden")
        print("  3) Beenden \n")

    def match_startup_menu_option(self):
        match int(input("\nOption eingeben: ")):
            case 1:
                self.create_new_database()
            case 2:
                self.use_existing_database()
            case 3:
                exit()

    def create_new_database(self):
        self.__db.set_name(str(input("Bitte geben sie den Namen der zu erstellenden Datenbank ein:")))
        self.run_db_menu()


    def use_existing_database(self):
        self.__db.set_name(str(input("Bitte geben sie den Namen der bereits existierenden Datenbank ein:")))
        self.run_db_menu()

    def run_db_menu(self):
        self.__db_menu_option = 0
        while(self.__db_menu_option != 5):    
            self.show_db_menu()
            self.match_db_menu_option()
            self.dump_database()

    def show_db_menu(self):
            print("\n=============================================")
            print("               Passwordmanager " + self.__db.get_name())
            print("=============================================")
            print("  1) Bereits existierende Passwörter anzeigen")
            print("  2) Neues Passwort hinzufügen")
            print("  3) Bereits existierendes Passwort löschen")
            print("  4) Passwort aktualisieren")
            print("  5) Abbruch\n")

            self.__db_menu_option = int(input("\nOption eingeben: "))

    def match_db_menu_option(self):
        match self.__db_menu_option:
            case 1:
                self.show_db()
            case 2:
                self.add_new_password()
            case 3:
                self.delete_password()
            case 4:
                self.update_password()
            case 5:
                pass

    def show_db(self):
        print("\n=============================================")
        print("URL          Name        Passwort       Notiz")
        print("=============================================")
        for line in self.__db.get_list():
            print(line)

    def add_new_password(self):
        url = str(input("URL: "))
        name = str(input("Name: "))
        password = str(input("Passwort: "))
        note = str(input("Notiz: "))

        entry = {
            "url": url,
            "name": name,
            "password": password,
            "note": note
        }

        self.__db.add_to_list(entry)

    def delete_password(self):
        url = str(input("URL des zu löschenden Passworts: "))
        list_copy = self.__db.get_list().copy()
        is_deleted = False

        for line in self.__db.get_list():
            if line.get("url") == url:
                list_copy.remove(line)
                is_deleted = True

        if is_deleted:
            self.__db.set_list(list_copy)
            print("Löschen erfolgreich")
        else:
            print("URL nicht gefunden")

    def update_password(self):
        url = str(input("URL des zu ändernden Passworts: "))
        password = str(input("Neues Passwort: "))
        list_copy = self.__db.get_list().copy()
        count_updates = 0

        for line in self.__db.get_list():
            if line.get("url") == url:
                line["password"] = password
                count_updates += 1
            
        print(str(count_updates) + " Passwörter geändert")
        
    def dump_database(self):
        json_name = self.__db.get_name() + ".json"
        with open(json_name, "w") as outfile:
            outfile.write(json.dumps(self.__db.get_list(), indent=2))

pw_manager = passwordmanager()
pw_manager.main()