from db_interface import DbInterface

class FakeDb(DbInterface):
    def __init__(self):
        self.__db = [
            {
            "name": "leon",
            "password": "123",
            "url": "www.123.de",
            "note": ""
            },
            {
            "name": "hannes",
            "password": "321",
            "url": "www.321.de",
            "note": "hannes"
            }
        ]

    def get_db_name(self) -> str:
        return self.__db_name

    def set_db_name(self, db_name):
        self.db_name = db_name    

    def get_db(self) -> tuple: 
        return self.__db

    def set_db(self, db):
        self.__db = db
