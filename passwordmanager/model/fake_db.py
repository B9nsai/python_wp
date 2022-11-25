class Fake_db:
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

    def get_db(self):
        return self.__db

    def set_db(self, db):
        self.__db = db
