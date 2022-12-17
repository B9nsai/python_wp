class database:
    def __init__(self):
        pass

    def get_name(self):
        return self.__name
        
    def set_name(self, db_name: str):
        self.__name = db_name

    def get_list(self):
        return self.__list

    def set_db_list(self, db_list: list):
        self.__list = db_list