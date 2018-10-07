"""
User story 34 list all couples who were married when the older spouse was more than twice the age as the younger spouse.

@author: Besnik Balaj
"""

from lib.user_story import UserStory

class UserStory34(UserStory):

    def print_rows(self, rows):
        for row in rows:
            if int(row[1]) >= (2*int(row[4])):
                print('REPORT: FAMILY: US34: Husband {} and Wife {} married where Husband was more than twice the age as Husband.'.format(row[0], row[3]))
            elif int(row[4]) >= (2*int(row[1])):
                print('REPORT: FAMILY: US34: Husband {} and Wife {} married where Wife was more than twice the age as Husband.'.format(row[0], row[3]))
            else:
                print('REPORT: FAMILY: US34: Husband {} and Wife {} married at reasonable age differences.'.format(row[0], row[3]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        Spouses = []

        #grab records of spouses
        Husb = c.execute('SELECT INDI.ID, Age, Married FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID) WHERE AGE != "NA" AND Married != "NA"').fetchall()
        Wife = c.execute('SELECT INDI.ID, Age, Married FROM FAM INNER JOIN INDI ON (FAM."Wife ID" = INDI.ID) WHERE AGE != "NA" AND Married != "NA"').fetchall()

        #Assummed a wife needs to present for husband and marriage to exist
        for i in range(len(Husb)):
            Spouses.append(Husb[i] + Wife[i])
        return Spouses
