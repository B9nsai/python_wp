#!/usr/bin/python3
import sys
import json

sys.path.append('model')
sys.path.append('view')
sys.path.append('controller')

from view import passwordmanager_ui as ui
from model import fake_db

class Passwordmanager:
    def __init__(self):
        self.action = 0
    


    def run(self):
        while True:
            ui.show_startup_menu()
            self.action = self.read_menu_action()
            print("")
            self.switch_action()

passwordmanager = Passwordmanager()
passwordmanager.run()