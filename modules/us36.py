"""
User story 36 prints all individuals who died in the last 30 days

@author: Michael Ameer
"""

from lib.user_story import UserStory
from datetime import datetime, timedelta
from lib.utilities import is_upcoming

class UserStory36(UserStory):
    
    def print_rows(self, rows):
        for row in rows:
            print('ALERT: INDIVIDUAL: US36: User {} died on {} in the last 30 days'.format(row[0], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        
        rows = c.execute('SELECT ID, Death FROM INDI WHERE Death != "NA"').fetchall()
        for row in rows:
            today = datetime.today()
            deat =  datetime.strptime(row[1], '%Y-%m-%d')
            difference = today - deat
            years = difference // timedelta(days=365.25)
            if (years <= 1):
                if(is_upcoming(datetime.strptime(row[1], '%Y-%m-%d'), datetime.today(), 30, 'days')) == True:
                    res.append(row)     
        return res


