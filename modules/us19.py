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

        #gather up all of the families where we have enough data to do this
        families = c.execute('SELECT ID, "Husband ID", "Wife ID" FROM FAM JOIN CHLD ON (ID = FAM_ID) WHERE ("Husband ID" != "NA" AND "Wife ID" != "NA")').fetchall()
        for family in families:

            #for every family, see if the husband and wife's parents are siblings
            husband_parents = c.execute('SELECT "Husband ID", "Wife ID" FROM CHLD JOIN FAM ON (FAM."Husband ID" = INDI_ID)').fetchone()
            wife_parents = c.execute('SELECT "Husband ID", "Wife ID" FROM CHLD JOIN FAM ON (FAM."Wife ID" = INDI_ID)').fetchone()

            if(husband_parents and wife_parents):
                husb_mother_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(husband_parents[0])).fetchone()
                husb_father_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(husband_parents[1])).fetchone()
                wife_father_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(wife_parents[0])).fetchone()
                wife_mother_fam = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(wife_parents[1])).fetchone()

                if(husb_mother_fam and husb_father_fam and wife_father_fam and wife_mother_fam):
                    if(husb_mother_fam[0] == wife_father_fam[0] or husb_mother_fam[0] == wife_mother_fam[0] or husb_father_fam[0] == wife_father_fam[0] or husb_father_fam[0] == wife_mother_fam[0]):
                        res.append(family)
                    
        return res