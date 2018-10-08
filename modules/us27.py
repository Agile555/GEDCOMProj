"""
User story 27 simply denotes the age of the users.  This is mainly done in the parser file, so the user story itself is not very large

@author: Mark Freeman
"""

from lib.user_story import UserStory

class UserStory27(UserStory):

    def print_rows(self, rows):
        pass
    
    def get_rows(self, conn):
        c = conn.cursor()
        rows = c.execute('SELECT Age FROM INDI').fetchall();
        return rows