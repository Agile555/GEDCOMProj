"""
User story 35 prints all individuals who were born in the last 30 days

@author: Michael Ameer
"""

from lib.user_story import UserStory
from datetime import datetime
from lib.utilities import is_upcoming

class UserStory35(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: INDIVIDUAL: US35: User {} was born on {} in the last 30 days'.format(row[0], row[1], row[2]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        rows = c.execute('SELECT ID, Birthday, Age FROM INDI WHERE (Birthday != "NA" AND Age != "NA")').fetchall()
        for row in rows:
            if(int(row[2]) == 0 and is_upcoming(datetime.strptime(row[1], '%Y-%m-%d'), datetime.today(), 30, 'days')):
                res.append(row)
        return res
