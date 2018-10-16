"""
User story 19 prints all marriages between first cousins

@author: Mark Freeman
"""

from lib.user_story import UserStory

class UserStory19(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ALERT: FAMILY: US19: Family {} has found to be between first cousins {} and {}'.format(row[0], row[1], row[2]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        husband_families = c.execute('SELECT cousins.ID, cousins."Husband ID", cousins."Wife ID", parents."Husband ID", parents."Wife ID" FROM FAM AS parents JOIN CHLD ON (parents."Husband ID" = INDI_ID) JOIN FAM AS cousins ON(FAM_ID = cousins.ID)').fetchall();
        wife_families = c.execute('SELECT parents."Husband ID", parents."Wife ID" FROM FAM AS parents JOIN CHLD ON (parents."Wife ID" = INDI_ID) JOIN FAM AS cousins ON(FAM_ID = cousins.ID)')
        """
        cousins.ID: Id of the family in question.  This is a marriage between two people who are supposedly cousins
        cousins.Husband ID: The male cousin in question
        cousins.Wife ID: The female cousin in question
        parents.Husband ID: The husband's father's ID
        parents.Wife ID: The husband's wife's ID
        We'll need to repeat this query again for the wife and check for any "NA" values
        """
        for husband_family, wife_family in zip(husband_families, wife_families):
            husband_mother_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(husband_family[3])).fetchone()
            husband_father_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(husband_family[4])).fetchone()
            wife_mother_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(wife_family[0])).fetchone()
            wife_father_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(wife_family[1])).fetchone()

            if((husband_mother_fam and wife_mother_fam) and (husband_mother_fam[0] == wife_mother_fam[0])): res.append(husband_family[0:3]) 
            elif((husband_mother_fam and wife_father_fam) and (husband_mother_fam[0] == wife_father_fam[0])): res.append(husband_family[0:3]) 
            elif((husband_father_fam and wife_mother_fam) and (husband_father_fam[0] == wife_mother_fam[0])): res.append(husband_family[0:3]) 
            elif((husband_father_fam and wife_father_fam) and (husband_father_fam[0] == wife_father_fam[0])): res.append(husband_family[0:3]) 
                    
        return res