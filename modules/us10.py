"""
User story 10 reports if marriage between husband and wife occurred before both were at least 14 years of age

@author: Besnik Balaj
"""
from datetime import datetime, timedelta
from lib.user_story import UserStory

class UserStory10(UserStory):

    def print_rows(self, rows):
        if rows == []:
            print('REPORT: FAMILY: US10: Family exists but did not contain a Husband or Wife or neither')
        else:
            for row in rows:
                if int(row[1]) <= 14 and int(row[3]) <= 14:
                    print('REPORT: FAMILY: US10: Husband {} married his Wife {} before either were at least 14 years of age. Husband was {} and the Wife was {}.'.format(row[0], row[2], row[1], row[3]))
                elif int(row[1]) <= 14:
                    print('REPORT: FAMILY: US10: Husband {} married his Wife {} before Husband was at least 14 years of age. Husband was {}.'.format(row[0], row[2], row[1]))
                elif int(row[3]) <= 14:
                    print('REPORT: FAMILY: US10: Husband {} married his Wife {} before Wife was at least 14 years of age. Wife was {}'.format(row[0], row[2], row[3]))
                else:
                    pass

    def get_rows(self, conn):
        c = conn.cursor()
        Spouses = []
        Spouse_Info = []

        #grab records of spouses
        Husb = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA" AND FAM."Husband ID" != "NA"  AND FAM."Wife ID" != "NA"').fetchall()
        Wife = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Wife ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA" AND FAM."Husband ID" != "NA"  AND FAM."Wife ID" != "NA"').fetchall()
        #0-ID,1-HusbBirt,2-MarriageDate,3-ID,4-WifeBirt,5-Marriage
        if (len(Husb) == len(Wife)):
            for i in range(len(Husb)):
                Spouses.append(Husb[i] + Wife[i])
            for fam in Spouses:
                HusbAge = str((datetime.strptime(fam[2],"%Y-%m-%d") - datetime.strptime(fam[1],"%Y-%m-%d")) // timedelta(days=365.2425))
                WifeAge = str((datetime.strptime(fam[2],"%Y-%m-%d") - datetime.strptime(fam[4],"%Y-%m-%d")) // timedelta(days=365.2425))
                Spouse_Info.append((fam[0],HusbAge,fam[3],WifeAge))

        return Spouse_Info
