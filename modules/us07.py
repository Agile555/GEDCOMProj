"""
User Story 07 ensures that no person be over 150 years of age.

@author: Besnik Balaj
"""

from user_story import UserStory

class UserStory07(UserStory):

    def print_rows(self, rows):
        for row in rows:
            if row[1] != "NA":
                print('ERROR: Death is greater than 150 years after birth for ' + row[0])
            else:
                print('ERROR: Current date is not less than 150 years after birth for ' + row[0])

    def get_rows(self, conn):
        c = conn.cursor()
        rows = c.execute('SELECT ID, Death FROM INDI WHERE Age > 150').fetchall()
        return rows