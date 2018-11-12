"""
User story 13 assures that siblings are more than 8 months apart or less than 2 days apart.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from lib.utilities import parse_string, nearby

class UserStory13(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print(row)
            print(len(row))
            print('CURIOSITY: FAMILY: US13: Family {} has strange sibling spacing between children {} and {} born on {}, and {}'.format(row[0], row[1], row[2], row[3], row[4]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        families = c.execute('SELECT ID FROM FAM WHERE Children != "NA"').fetchall() or []
        for family in families:
            children = c.execute('SELECT INDI_ID, Birthday FROM CHLD JOIN INDI ON (INDI.ID = INDI_ID) WHERE (Birthday != "NA" AND FAM_ID = "{}")'.format(family[0])).fetchall() or []
            if(len(children) > 1):
                #we have no choice to go O(n^2), was thinking we could go O(n log n) by sorting and then comparing only adjacent values (one pass)
                #but non-adjacent ones can also match in that case.  For example, if we had three of the same birthday, then we would get:
                #(1, 2), (2, 3) AND (1, 3)
                for i in range(len(children) - 1):
                    for j in range(i + 1, len(children)):
                        a, b = parse_string(children[i][1]), parse_string(children[j][1]) #get birthdays
                        if(not nearby(a, b, 1, 'days') and nearby(a, b, 8, 'months')):
                            res.append((family[0], children[i][0], children[j][0], children[i][1], children[j][1]), )

        return res