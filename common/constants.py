from abc import ABC
from enum import Enum


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5


class Person(ABC):
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone


class Constants:
    def __init__(self):
          self.MAX_BOOKS_ISSUED_TO_A_USER = 5
          self.MAX_LENDING_DAYS = 10

