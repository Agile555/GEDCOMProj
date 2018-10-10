"""
User story 30 prints all living married people

@author: Kipsy Quevada
"""

from lib.user_story import UserStory

class UserStory30(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: INDIVIDUAL: US30: User {} is married'.format(row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        rows = c.execute('SELECT INDI.ID FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID OR FAM."Wife ID" = INDI.ID) WHERE Married != "NA"').fetchall()
        for row in rows:
            res.append(row)
        return res
