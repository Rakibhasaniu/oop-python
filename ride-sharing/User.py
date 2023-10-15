from abc import ABC,abstractclassmethod
class User(ABC):
    def __init__(self,name,email) -> None:
        self.name = name
        self.email = email
        #TODO: set user id dynamically
        self.__id = 0