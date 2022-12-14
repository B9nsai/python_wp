#!/usr/bin/python3
import sys
import json

sys.path.append('model')
sys.path.append('view')
sys.path.append('controller')

from view import passwordmanager_ui as ui
from model import fake_db
from controller import Controller

class Passwordmanager:
    def __init__(self):
        self.controller = Controller()

    
    def run(self):
        self.controller.run()

def main():
    passwordmanager = Passwordmanager()
    passwordmanager.run()

main()
