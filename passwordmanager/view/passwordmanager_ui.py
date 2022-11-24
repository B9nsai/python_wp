import sys
sys.path.append('../controller')

from controller import controller

def show_startup_menu():
    print("=============================================")
    print("               Passwordmanager               ")
    print("=============================================")
    print("  1) Neue Passwortdatenbank erstellen        ")
    print("  2) Existierende Passwortdatenbank verwenden")
    print("  3) Abbruch \n")

def show_db_menu():
        print("=============================================")
        print("               Passwordmanager " + controller.db_name)
        print("=============================================")
        print("  1) Bereits existierende Passwörter anzeigen")
        print("  2) Neues Passwort hinzufügen")
        print("  3) Bereits existierendes Passwort löschen")
        print("  4) Passwort aktualisieren")
        print("  5) Beenden\n")