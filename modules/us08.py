"""
User story 08 assures that children are born after their parents are married.
(in my mormon GEDCOM)

@author: Mark Freeman, Besnik Balaj
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory08(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: Marriage on {} occurs after child {} born on {} for family {}.'.format(row[2], row[0], row[3], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        rows = c.execute('SELECT CHLD.INDI_ID, FAM.ID, FAM.Married, INDI.Birthday FROM CHLD INNER JOIN FAM ON (FAM.ID = CHLD.FAM_ID) INNER JOIN INDI ON (INDI.ID = CHLD.INDI_ID) WHERE Married != "NA"').fetchall()
        for row in rows:
            if(datetime.strptime(row[2], '%Y-%m-%d') > datetime.strptime(row[3], '%Y-%m-%d')):
                res.append(row)
        return res