"""
User story 05 prints an error if any individuals are found to have gotten married after their death.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory05(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: INDIVIDUAL: US05: Marriage on {} occurs after death on {} for user {}'.format(row[1], row[2], row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        
        #grab all records where we have a spouse that has both died and been married
        rows = c.execute('SELECT INDI.ID, Married, Death FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID OR FAM."Wife ID" = INDI.ID) WHERE (Death != "NA" AND Married != "NA")').fetchall()
        for row in rows:
            #TODO add test cases which have NA marriage, death dates
            
            if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #if marriage after death
                res.append(row)
        return res