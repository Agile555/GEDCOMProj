"""
User story 12 prints an error if the mother is greater than
or equal to 60 years older than her children, or the father
is greater than or equal to 80 years older than his children.

@author: Kipsy Quevada, Besnik Balaj
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory12(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('REPORT: INDIVIDUAL: US12: Parent {} is too too old for child {}.'.format(row[0], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        father = []
        mother = []
        children = c.execute('SELECT CHLD.INDI_ID, INDI.Age, FAM."Husband ID", FAM."Wife ID" FROM CHLD INNER JOIN INDI ON (INDI.ID = CHLD.INDI_ID) INNER JOIN FAM ON (CHLD.FAM_ID = FAM.ID) WHERE FAM_ID != "NA" AND INDI_ID != "NA" AND INDI.Age > 0 AND INDI.Age != "NA"').fetchall()
        for child in children:
            # Assumed that there is only one father and one mother.
            father = c.execute('SELECT ID, Age FROM INDI WHERE Age != "NA" AND Age > 0 AND ID = "{}"'.format(child[2])).fetchall()
            mother = c.execute('SELECT ID, Age FROM INDI WHERE Age != "NA" AND Age > 0 AND ID = "{}"'.format(child[3])).fetchall()
            if int(father[0][1]) >= int(child[1]) + 80: #get the ages and compare
                res.append((father[0][0], child[0]))
            if int(mother[0][1]) >= int(child[1]) + 60: #get the ages and compare
                res.append((mother[0][0], child[0]))
        return res