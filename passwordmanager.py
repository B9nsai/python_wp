#!/usr/bin/python3

class Passwordmanager:
    def __init__(self):
        pass

    def show_menu(self):
        print("=============================================")
        print("               Passwordmanager               ")
        print("=============================================")
        print("  1) Neue Passwortdatenbank erstellen        ")
        print("  2) Existierende Passwortdatenbank verwenden")
        print("  3) Abbruch \n")

    def read_menu_action(self):
        return input("Was möchten sie tun? ")

    def run(self):
        self.show_menu()
        self.read_menu_action()

passwordmanager = Passwordmanager()
passwordmanager.run()


