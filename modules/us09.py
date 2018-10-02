"""
User story 09 assures that there are no individuals who were born over 9 months after the death of their father
or were born after the death of their mother

@author: Mark Freeman
"""

from lib.user_story import UserStory
from datetime import datetime, timedelta

class UserStory09(UserStory):

    def print_rows(self, rows):
        for row in rows:
            if(row[3] == 'Husband'): #different messages for husband and wife
                print('ERROR: INDIVIDUAL: US09: Individual {} found to have been born over 9 months after death of father {} in family {}'.format(row[1], row[2], row[0]))
            else: #must be a wife
                print('ERROR: INDIVIDUAL: US09: Individual {} found to have been born after death of mother {} in family {}'.format(row[1], row[2], row[0]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        #have to do this in multiple queries, as the birthday for the child and the death of the parents are two completely different
        #rows on the INDI table

        #gather up all of the children who have a father listed
        rows = c.execute('SELECT FAM.ID, INDI_ID, FAM."Husband ID" FROM CHLD INNER JOIN FAM ON (FAM_ID = FAM.ID) INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID) WHERE (FAM."Husband ID" != "NA")').fetchall()

        #now go and get both the birthday of the child as well as the date of death of the father
        for row in rows:
            birthday = c.execute('SELECT Birthday FROM INDI WHERE (ID = "{}" AND Birthday != "NA")'.format(row[1])).fetchone() #TODO: why does adding the "not NA" contraint not fix this?
            death = c.execute('SELECT Death FROM INDI WHERE (ID = "{}" AND Death != "NA")'.format(row[2])).fetchone()

            #only bother checking if we have a birthday for the child and a death for the father
            if(birthday and death):
                #TODO: technically not right as 9 months could be a different number of days depending on where in the year it starts
                if(datetime.strptime(birthday[0], '%Y-%m-%d') > (datetime.strptime(death[0], '%Y-%m-%d') + timedelta(days=270))): #TODO: add test cases for NA birthday and death
                    res.append(row + ('Husband', ))

        #now we do the same, but with the mothers
        rows = c.execute('SELECT FAM.ID, INDI_ID, FAM."Wife ID" FROM CHLD INNER JOIN FAM ON (FAM_ID = FAM.ID) INNER JOIN INDI ON (FAM."Wife ID" = INDI.ID) WHERE (FAM."Wife ID" != "NA")').fetchall()
        for row in rows:
            birthday = c.execute('SELECT Birthday FROM INDI WHERE (ID = "{}" AND Birthday != "NA")'.format(row[1])).fetchone()
            death = c.execute('SELECT Death FROM INDI WHERE (ID = "{}" AND Death != "NA")'.format(row[2])).fetchone()

            #only check if we have the child birthday and death date of the mother
            if(birthday and death):
                #TODO: again, technically not right
                if(datetime.strptime(birthday[0], '%Y-%m-%d') > datetime.strptime(death[0], '%Y-%m-%d')):
                    res.append(row + ('Wife', ))
        
        return res