"""
User story 06 prints an error if any individuals are found to have gotten divorced after their death.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory06(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: INDIVIDUAL: US06: Divorce on {} occurs after death on {} for user {}'.format(row[1], row[2], row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        
        #grab all records where we have a spouse that has both died and been married
        rows = c.execute('SELECT INDI.ID, Divorced, Death FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID OR FAM."Wife ID" = INDI.ID) WHERE (Death != "NA" AND Divorced != "NA")').fetchall()
        for row in rows:
            if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #if marriage after death
                res.append(row)
        return res