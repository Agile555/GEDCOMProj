"""
User story 29 prints all individuals who are deceased

@author: Michael Ameer
"""

from lib.user_story import UserStory
import sqlite3

class UserStory29(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print(rows)

    def get_rows(self, conn):
        c = conn.cursor()
        c.execute("SELECT ID FROM INDI WHERE Death != 'NA'")
        res = []
        row = c.fetchone()
        while(row):
            res.append(row[0])
            row = c.fetchone()
        return res
