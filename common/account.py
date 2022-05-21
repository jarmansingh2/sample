# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


from abc import ABC, abstractmethod
from datetime import datetime

from .constants import *

class Account(ABC):
    def __init__(self, id, name):
        self.__id = id
        self.__name = name


class User(Account):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__subscription: list = []

    def subscribe_news(self, news_type: str):
        self.__subscription.insert(news_type)


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)



