"""
User story 21 prints an error if the mother is not female
and the Husband is not Male.

@author: Besnik Balaj
"""

from lib.user_story import UserStory
from datetime import datetime

class UserStory21(UserStory):

    def print_rows(self, rows):
        for row in rows:
            if row[0] == 'F':
                print('REPORT: INDIVIDUAL: US21: Husband {} is the incorrect gender for their role, Individual is Female. when they should be Male'.format(row[1]))
            else:
                print('REPORT: INDIVIDUAL: US21: Wife {} is the incorrect gender for their role, Individual is Male. when they should be Female'.format(row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []

        HusbandGend = c.execute('SELECT INDI.Gender, FAM."Husband ID" FROM FAM INNER JOIN INDI ON (INDI.ID=Fam."Husband ID") WHERE INDI.Gender != "NA" AND Fam."Husband ID"!="NA"').fetchall()
        WifeGend = c.execute('SELECT INDI.Gender, FAM."Wife ID" FROM FAM INNER JOIN INDI ON (INDI.ID=Fam."Wife ID") WHERE INDI.Gender != "NA" AND Fam."Wife ID"!="NA"').fetchall()
        for HCheck in HusbandGend:
            if HCheck[0] == "F":
                res.append(HCheck)
        for WCheck in WifeGend:
            if WCheck[0] == "M":
                res.append(WCheck)
        return res
