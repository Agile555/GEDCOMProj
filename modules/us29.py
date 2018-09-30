"""
User story 29 prints all individuals who are deceased

@author: Michael Ameer
"""

from lib.user_story import UserStory
import sqlite3

class UserStory29(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: User {} is deceased.'.format(row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        rows = c.execute("SELECT ID FROM INDI WHERE Death != 'NA'").fetchall()
        for row in rows:
            res.append(row[0])
        return res
