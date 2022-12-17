class database:
    def __init__(self):
        self.__name = ""
        self.__list = []

    def get_name(self):
        return self.__name
        
    def set_name(self, db_name: str):
        self.__name = db_name

    def get_list(self):
        return self.__list

    def set_list(self, db_list: list):
        self.__list = db_list

    def add_to_list(self, entry: dict):
        self.__list.append(entry)