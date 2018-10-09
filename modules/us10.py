"""
User story 10 reports if marriage between husband and wife occurred before both were at least 14 years of age

@author: Besnik Balaj
"""
from datetime import datetime, timedelta
from lib.user_story import UserStory

class UserStory10(UserStory):

    def print_rows(self, rows):
        for row in rows:
            if int(row[2]) <= 14 and int(row[3]) <= 14:
                print('REPORT: FAMILY: US10: Husband {} married his Wife {} married before either were at least 14 years of age. Husband was {} and the Wife was {}.'.format(row[0], row[2], row[1], row[4]))
            elif int(row[2]) <= 14:
                print('REPORT: FAMILY: US10: Husband {} married his Wife {} married before Husband was at least 14 years of age. Husband was {}.'.format(row[0], row[2], row[1]))
            elif int(row[4]) <= 14:
                print('REPORT: FAMILY: US10: Husband {} married his Wife {} married before Wife was at least 14 years of age. Wife was {}'.format(row[0], row[2], row[4]))
            else:
                pass

    def get_rows(self, conn):
        c = conn.cursor()
        Spouses = []
        Spouse_Info = []

        #grab records of spouses
        Husb = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA"').fetchall()
        Wife = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Wife ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA"').fetchall()
        #0-ID,1-HusbBirt,2-MarriageDate,3-ID,4-WifeBirt,5-Marriage
        for i in range(len(Husb)):
            Spouses.append(Husb[i] + Wife[i])
        for fam in Spouses:
            HusbAge = str((datetime.strptime(fam[2],"%Y-%m-%d") - datetime.strptime(fam[1],"%Y-%m-%d")) // timedelta(days=365.2425))
            WifeAge = str((datetime.strptime(fam[2],"%Y-%m-%d") - datetime.strptime(fam[4],"%Y-%m-%d")) // timedelta(days=365.2425))
            for i in range(len(Spouses)):
                hold = [fam[0],HusbAge,fam[3],WifeAge]
                Spouse_Info.insert(i,hold)
                break
        return Spouse_Info
