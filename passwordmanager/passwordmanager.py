#!/usr/bin/python3
import sys
import json

sys.path.append('model')
sys.path.append('view')
sys.path.append('controller')

from view import passwordmanager_ui as ui
from model import fake_db
from controller import controller

class Passwordmanager:
    def __init__(self):
        self.startup_menu_action = 0
        self.controller = controller()
    
    def run(self):
        while True:
            ui.show_startup_menu()
            self.startup_menu_action = self.controller.read_startup_menu_action()
            print("")
            self.controller.switch_startup_menu_action()

passwordmanager = Passwordmanager()
passwordmanager.run()