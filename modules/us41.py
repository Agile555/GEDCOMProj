"""
User Story 41 allows parsing of incomplete dates

@author: Besnik Balaj
"""

from lib.user_story import UserStory

class UserStory41(UserStory):

    def print_rows(self, rows):
        pass

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        rows = c.execute('SELECT Birthday FROM INDI').fetchall() #if you only select one column, you don't get a tuple back
        for row in rows:
            res.append(row[0])
        return res