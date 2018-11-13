"""
User Story 42 allows rejection of illegitimate dates

@author: Besnik Balaj
"""

from lib.user_story import UserStory

class UserStory42(UserStory):

    def print_rows(self, rows):
        pass

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        rows = c.execute('SELECT ID FROM INDI where Birthday == "NA"').fetchall() #if you only select one column, you don't get a tuple back
        for row in rows:
            res.append(row[0])
        return res
