"""
User story 33 alerts the user to any individuals who are orphans.

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime, timedelta
import sqlite3

class UserStory33(UserStory):

    def print_rows(self, rows):
        for row in rows: #TODO: Need to figure out exactly what information we should be printing, rather it be as descriptive as possible, or as little as needed
            print('ALERT: Individual {} found to have become an orphan at age {}'.format(row[0], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        #go grab all of the children who have defined parents, otherwise don't bother
        rows = c.execute('SELECT INDI_ID, FAM."Husband ID", FAM."Wife ID" FROM CHLD INNER JOIN FAM ON (FAM_ID = ID) WHERE (FAM."Husband ID" != "NA" AND FAM."Wife ID" != "NA")').fetchall()
        for row in rows:
            birthday = c.execute('SELECT Birthday FROM INDI WHERE ID = "{}"'.format(row[0])).fetchone()
            husband_death = c.execute('SELECT Death FROM INDI WHERE (ID = "{}" AND Death != "NA")'.format(row[1])).fetchone()
            wife_death = c.execute('SELECT Death FROM INDI WHERE (ID = "{}" AND Death != "NA")'.format(row[2])).fetchone()

            #only bother checking the conditions if we have them
            if(birthday and husband_death and wife_death):
                birthday = datetime.strptime(birthday[0], '%Y-%m-%d')
                #we can't rely on the age attribute, as it will freeze once the child dies, must use his date of birth and the parents' date of death
                age_at_fathers_death = (datetime.strptime(husband_death[0], '%Y-%m-%d') - birthday).days // 365
                age_at_mothers_death = (datetime.strptime(wife_death[0], '%Y-%m-%d') - birthday).days // 365

                #if both parents died when he was under 18, he is an orphan
                if(age_at_fathers_death < 18 and age_at_mothers_death < 18):
                    res.append((row[0], str(max(age_at_fathers_death, age_at_mothers_death)))) #we don't need to convert to string here, but for consistency with other tests

        return res