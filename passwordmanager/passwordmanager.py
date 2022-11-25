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
        self.controller = controller()
    
    def run(self):
        while True:
            self.controller.run_startup_menu()
            

passwordmanager = Passwordmanager()
passwordmanager.run()
