"""
User story 23 prints an error if there are
individuals with the same name and birthday
@author: Michael Ameer
"""

from lib.user_story import UserStory

class UserStory23(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: INDIVIDUAL: US23: Individual {} and individual {} both have the same name and birthday.'.format(row[0], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        individual = []
        individual = c.execute('SELECT ID, Name, Birthday FROM INDI WHERE Name != "NA" and Birthday != "NA"').fetchall()
        for i, indi in enumerate(individual):
            for indi2 in individual[i+1:]:
                if indi[1:] == indi2[1:]:
                    res.append((indi[0], indi2[0]))
        return res
