"""
User story 02 prints an error if any individuals of the database are found to have a birth
data that occurs after they were married.

@author: Kipsy Quevada, pair programmed with Besnik Balaj
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory02(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: Birthday on {} occurs after marriage on {} for user {}'.format(row[1], row[2], row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        rows = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID OR FAM."Wife ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA"').fetchall()
        for row in rows:
            if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #get the birth and marriage and compare dates
                res.append(row)
        return res