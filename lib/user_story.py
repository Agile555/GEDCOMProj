"""
Abstract class from which to extend user stories.  All methods declared abstract must be overridden in their subclass.

@author: Mark Freeman
"""

from abc import ABC, abstractmethod

class UserStory(ABC):
    
    def fire(self, conn):
        rows = this.get_rows(self, conn)
        this.print_rows(self, rows)
    
    @abstractmethod
    def get_rows(self, conn):
        pass

    @abstractmethod
    def print_rows(self, rows):
        pass