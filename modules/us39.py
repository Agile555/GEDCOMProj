"""
User story 39 alerts the user to any upcoming anniversaries.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime
from lib.utilities import is_upcoming

class UserStory39(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: FAMILY: US39: Family {} has an anniversary within the next 30 days on {}'.format(row[0], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        #same exact logic as US38, just with families.  With families, marriage and divorce are pretty much analogous to marriage and divorce
        #go round up all of the families who were married and never got divorced
        rows = c.execute('SELECT ID, "Husband ID", "Wife ID", Married FROM FAM WHERE (Married != "NA" AND Divorced = "NA")').fetchall()
        for row in rows:

            #before bothering to check if they're alive, make sure their annivesary would be coming up
            if(is_upcoming(datetime.today(), datetime.strptime(row[3], '%Y-%m-%d'), 30, 'days')):
                #make sure both people are alive to celebrate
                husband_alive = c.execute('SELECT ID FROM INDI WHERE (ID = "{}" AND Death = "NA")'.format(row[1])).fetchone()
                wife_alive = c.execute('SELECT ID FROM INDI WHERE (ID = "{}" AND Death = "NA")'.format(row[2])).fetchone()
                if(husband_alive and wife_alive):
                    res.append((row[0], row[3]))
            
        return res