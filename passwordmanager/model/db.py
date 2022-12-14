from db_interface import DbInterface

class Db(DbInterface):
    def __init__(self):
        self.__db = []

    def get_db_name(self) -> str:
        return self.__db_name

    def set_db_name(self, db_name):
        self.__db_name = db_name

    def get_db(self) -> tuple:
        return self.__db

    def set_db(self, db):
        self.__db = db


