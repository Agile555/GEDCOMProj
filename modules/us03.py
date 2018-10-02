"""
User story 03 prints an error if any individuals of the database are found to have a birth
data that occurs after they have died.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory03(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: INDIVIDUAL: US03: Birthday on {} occurs after death on {} for user {}'.format(row[1], row[2], row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        rows = c.execute('SELECT ID, Birthday, Death FROM INDI WHERE Birthday != "NA" AND Death != "NA"').fetchall()
        for row in rows:
            if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #get the birth and death and compare dates
                res.append(row)
        return res
