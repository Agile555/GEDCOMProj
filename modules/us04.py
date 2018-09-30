"""
User story 04 prints an error if a family is found to have gotten divorced before they were married.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory04(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: Divorce on ' + row[2] + ' occurs before marriage on ' + row[1] + ' for family ' + row[0])

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        
        #grab all records where we have a spouse that has both died and been married
        rows = c.execute('SELECT ID, Married, Divorced FROM FAM WHERE (Married != "NA" AND Divorced != "NA")').fetchall()
        for row in rows:
            if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #if marriage after divorce
                res.append(row)
        return res