import sys
sys.path.append('../controller')

from controller import Controller

def show_startup_menu():
    print("\n=============================================")
    print("               Passwordmanager               ")
    print("=============================================")
    print("  1) Neue Passwortdatenbank erstellen        ")
    print("  2) Existierende Passwortdatenbank verwenden")
    print("  3) Abbruch \n")

def show_db_menu(db_name):
        print("\n=============================================")
        print("               Passwordmanager " + db_name)
        print("=============================================")
        print("  1) Bereits existierende Passwörter anzeigen")
        print("  2) Neues Passwort hinzufügen")
        print("  3) Bereits existierendes Passwort löschen")
        print("  4) Passwort aktualisieren")
        print("  5) Beenden\n")

def show_db(db):
    print("\n=============================================")
    print("URL          Name        Passwort       Notiz")
    print("=============================================")
    for line in db.get:
        print(line)
