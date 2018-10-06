"""
User story 38 alerts the user to any upcoming birthdays.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime
from lib.utilities import is_upcoming

class UserStory38(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: INDIVIDUAL: US38: User {} has a birthday within the next 30 days on {}').format(row[0], row[1])

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        rows = c.execute('SELECT ID, Birthday FROM INDI WHERE (Birthday != "NA" AND Death = "NA")').fetchall()
        for row in rows:
            if(is_upcoming(datetime.today(), datetime.strptime(row[1], '%Y-%m-%d'), 30, 'days')):
                res.append(row)
        return res