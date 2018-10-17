"""
User story 34 list all couples who were married when the older spouse was more than twice the age as the younger spouse.

@author: Besnik Balaj
"""

from datetime import datetime, timedelta
from lib.user_story import UserStory

class UserStory34(UserStory):

    def print_rows(self, rows):
        if rows == []:
            print('REPORT: FAMILY: US34: Family exists but did not contain a Husband or Wife or neither')
        else:
            for row in rows:
                if int(row[1]) >= (2*int(row[3])):
                    print('REPORT: FAMILY: US34: Husband {} and Wife {} married where Husband was more than twice the age as Husband. Husband was {} while Wife was {}'.format(row[0], row[2], row[1], row[2]))
                elif int(row[3]) >= (2*int(row[1])):
                    print('REPORT: FAMILY: US34: Husband {} and Wife {} married where Wife was more than twice the age as Husband. Husband was {} while Wife was {}'.format(row[0], row[2], row[1], row[2]))
                else:
                    print('REPORT: FAMILY: US34: Husband {} and Wife {} married at reasonable age differences. Husband was {} while Wife was {}'.format(row[0], row[2], row[1], row[2]))

    def get_rows(self, conn):
        c = conn.cursor()
        Spouses = []
        Spouse_Info = []

        #grab records of spouses
        Husb = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA"').fetchall()
        Wife = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Wife ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA"').fetchall()
        if len(Husb) == len(Wife):
            for i in range(len(Husb)):
                Spouses.append(Husb[i] + Wife[i])
            for fam in Spouses:
                HusbAge = str((datetime.strptime(fam[2],"%Y-%m-%d") - datetime.strptime(fam[1],"%Y-%m-%d")) // timedelta(days=365.2425))
                WifeAge = str((datetime.strptime(fam[2],"%Y-%m-%d") - datetime.strptime(fam[4],"%Y-%m-%d")) // timedelta(days=365.2425))
                Spouse_Info.append((fam[0],HusbAge,fam[3],WifeAge))
        return Spouse_Info
