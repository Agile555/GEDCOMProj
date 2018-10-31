"""
User story 24 prints an error if more than one family
with the same spouses by name and the same marriage
date appear in a GEDCOM file

@author: Kipsy Quevada
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory24(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: FAMILY: US24: Family {} and family {} both have the same spouses by name and marriage date.'.format(row[0], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        family = []
        family = c.execute('SELECT ID, Married, "Husband Name", "Wife Name" FROM FAM WHERE Married != "NA" AND "Husband Name" != "NA" AND "Wife Name" != "NA"').fetchall()
        for i, fam in enumerate(family):
            for fam2 in family[i+1:]:
                if fam[1:] == fam2[1:]:
                    res.append((fam[0], fam2[0]))
        return res