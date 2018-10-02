"""
User story 31 prints all individuals who are single AND over 30 years old

@author: Michael Ameer, Mark Freeman
"""

from lib.user_story import UserStory

class UserStory31(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: INDIVIDUAL: US31: Individual {} is both single and over age 30'.format(row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        rows = c.execute('SELECT ID, Age FROM INDI WHERE Spouse == "NA" AND Age != "NA"').fetchall()
        for row in rows:
            if(int(row[1]) > 30):
                res.append(row)
        return res
