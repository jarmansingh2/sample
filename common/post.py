# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


from abc import ABC, abstractmethod
from datetime import datetime

from .constants import *

class Post(ABC):
    def __init__(self, id, post_type, content, optional_category):
        self.__id = id
        self.__post_type = post_type
        self.__content = content
        self.__optional_category = optional_category
        self.__vote = 0

    def add_upvote(self):
        self.__vote += 1

    def add_downvote(self):
        self.__vote -= 1

    def get_content(self):
        return self.__content
