"""
User Story 28 lists siblings in families by decreasing age

@author: Kipsy Quevada, Mark Freeman
"""

from lib.user_story import UserStory

class UserStory28(UserStory):

    def print_rows(self, rows):
        pass

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        rows = c.execute('SELECT Children FROM FAM').fetchall() #if you only select one column, you don't get a tuple back
        for row in rows:
            res.append(row[0])
        return res