"""
User story 01 prints an error if dates (birth, marriage, divorce, death) are after the current date

@author: Kipsy Quevada
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory01(UserStory):
    
    def print_rows(self, rows):
        for row in rows:
            print ("ERROR: INDIVIDUAL: US01: Individual {} with date {} occurs after the current date".format(row[0], row[1]))
    
    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        rows = c.execute("select ID, Birthday from INDI where Birthday > date('now') AND Birthday != 'NA'").fetchall()
        rows += c.execute("select ID, Married from FAM where Married > date('now') AND Married != 'NA'").fetchall()
        rows += c.execute("select ID, Divorced from FAM where Divorced > date('now') AND Divorced != 'NA'").fetchall()
        rows += c.execute("select ID, Death from INDI where Death > date('now') AND Death != 'NA'").fetchall()
        for row in rows:
            res.append(row)
        return res