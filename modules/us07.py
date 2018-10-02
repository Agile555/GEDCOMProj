"""
User Story 07 ensures that no person be over 150 years of age.

@author: Besnik Balaj
"""

from lib.user_story import UserStory

class UserStory07(UserStory):

    def print_rows(self, rows):
        for row in rows:
            if row[1] != "NA":
                print('ERROR: Death is greater than 150 years after birth for {}'.format(row[0]))
            else:
                print('ERROR: Current date is not less than 150 years after birth for {}'.format(row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        rows = c.execute('SELECT ID, Death, Age FROM INDI WHERE Age != "NA" ').fetchall()
        res = []
        for row in rows:
            if int(row[2]) > 150:
                res.append(row)
        return res
