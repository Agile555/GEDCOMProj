"""
User story 32 alerts the user to a large amount of siblings born at once (over 4)

@author: Mark Freeman
"""

from collections import Counter
from lib.user_story import UserStory
from lib.utilities import parse_string, format_date, fast_forward
from datetime import datetime, timedelta

class UserStory32(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: FAMILY: US32: Family {} found to have many children born closely on {}'.format(row[0], ', '.join(row[1])))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        d = {}
        #grab all families with over 4 children that have listed birthdays (we don't want to run this algorithm on the whole set)
        families = c.execute('SELECT FAM_ID FROM CHLD INNER JOIN INDI ON (INDI_ID = INDI.ID) WHERE (Birthday != "NA") GROUP BY FAM_ID HAVING (COUNT(*) > 4)').fetchall()
        for family in families:
            children = c.execute('SELECT Birthday FROM CHLD INNER JOIN INDI ON (FAM_ID = "{}" AND INDI_ID = INDI.ID)'.format(family[0])).fetchall()
            for child in children:
                #we need to construct a counter to count birthdays
                if(d.get(family[0])):
                    d[family[0]][child[0]] += 1
                else:
                    d[family[0]] = Counter([child[0]])

        #Now we have all of our birthdays loaded in with counts.  Now search the dict and collapse any dates which occur within a day of each other
        for family in list(d.keys()):
            #if the family has over 4 kids on the same date, flag it immediately
            for date in list(d[family].keys()):
                num_siblings = d[family][date]
                if(num_siblings > 4):
                    res.append((family, [date]))
                else:
                    #if not, check for an adjacent date and see if it boosts it over 4
                    next_day = format_date(fast_forward(parse_string(date), 1, 'days'))
                    num_next_day = d[family].get(next_day)
                    if(num_next_day):
                        num_siblings = d[family][date] + num_next_day
                        if(num_siblings > 4):
                            res.append((family, [date, next_day]))

        return res