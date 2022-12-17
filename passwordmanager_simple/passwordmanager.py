#!/usr/bin/python3

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
        self.show_db_menu()
        self.match_db_menu_option()

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
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass

    def show_db(self):
        print("\n=============================================")
        print("URL          Name        Passwort       Notiz")
        print("=============================================")
        for line in self.__db.get_list():
            print(line)

pw_manager = passwordmanager()
pw_manager.main()