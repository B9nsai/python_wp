#!/usr/bin/python3
def main():
    while(True):
        run_startup_menu()

def run_startup_menu():
    show_startup_menu()
    switch_startup_menu_option()

def show_startup_menu():
    print("\n=============================================")
    print("               Passwordmanager               ")
    print("=============================================")
    print("  1) Neue Passwortdatenbank erstellen        ")
    print("  2) Existierende Passwortdatenbank verwenden")
    print("  3) Abbruch \n")

def switch_startup_menu_option():
    match int(input("\nOption eingeben: ")):
        case 1:
            create_new_database()
        case 2:
            use_existing_database()
        case 3:
            print("3")

def create_new_database():
    pass

def use_existing_database():
    pass

def show_db_menu(db_name):
        print("\n=============================================")
        print("               Passwordmanager " + db_name)
        print("=============================================")
        print("  1) Bereits existierende Passwörter anzeigen")
        print("  2) Neues Passwort hinzufügen")
        print("  3) Bereits existierendes Passwort löschen")
        print("  4) Passwort aktualisieren")
        print("  5) Beenden\n")

        int(input("\nOption eingeben: "))


def show_db(db):
    print("\n=============================================")
    print("URL          Name        Passwort       Notiz")
    print("=============================================")
    for line in db.get:
        print(line)

main()