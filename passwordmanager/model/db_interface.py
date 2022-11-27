from abc import ABC, abstractmethod

class DbInterface(ABC):
    @abstractmethod
    def get_db_name(self):
        return self.__db_name

    @abstractmethod
    def set_db_name(self, db_name):
        self.db_name = db_name
    
    @abstractmethod
    def get_db(self):
        return self.__db
    
    @abstractmethod
    def set_db(self, db):
        self.__db = db