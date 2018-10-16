"""
User story 18 prints all marriages between siblings

@author: Mark Freeman
"""

from lib.user_story import UserStory

class UserStory18(UserStory):

    def print_rows(self, rows):
        for row in rows:
            pass

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        #gather up all of the families
        families = c.execute('SELECT ID, "Husband ID", "Wife ID" FROM FAM JOIN CHLD ON (ID = FAM_ID) WHERE ("Husband ID" != "NA" AND "Wife ID" != "NA")').fetchall()
        for family in families:

            #for every family, see if the husband and wife come from the same family in the CHLD table
            husband = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(family[1])).fetchone()
            wife = c.execute('SELECT FAM_ID FROM CHLD WHERE INDI_ID = "{}"'.format(family[2])).fetchone()
            
            if(husband and wife): #if we have them, and they're the same, then add them in
                if(husband == wife):
                    res.append(family)
                    
        return res