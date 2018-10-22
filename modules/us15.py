"""
User story 15 reports all families that have more than 15 siblings.

@author: Besnik Balaj
"""

from lib.user_story import UserStory

class UserStory15(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('REPORT: FAMILY: US15: Family {} has too many children, specfically they have more than 15.'.format(row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        count = 0

        families = c.execute('SELECT FAM_ID, INDI_ID FROM CHLD WHERE INDI_ID != "NA"').fetchall()
        if families != []:
            hold = families[0][0]
        for fam in families:
            if fam[0] == hold:
                count += 1
            else:
                if count > 15:
                    res.append(hold)
                count = 1
                hold = fam[0] 
        if count > 15:
            res.append(hold)
        return res
