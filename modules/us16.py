"""
User story 16 prints an error if all male members
of a family do not have the same last name
@author: Michael Ameer
"""

from lib.user_story import UserStory

class UserStory16(UserStory):

    def print_rows(self, rows):
        for row in rows:
            print('ERROR: FAMILY: US16: Individual {} and individual {} of the same family have different last names.'.format(row[0], row[1]))

    def get_rows(self, conn):
        c = conn.cursor()
        res = []
        family = []
        family = c.execute('SELECT ID, "Husband ID", "Husband Name" FROM FAM WHERE ID != "NA"').fetchall()
        for fam in family:
            children = c.execute('SELECT INDI.ID, INDI.Name, INDI.Gender FROM CHLD INNER JOIN INDI ON (INDI.ID = CHLD.INDI_ID) INNER JOIN FAM ON (CHLD.FAM_ID = "{}") WHERE INDI.Name != "NA" and INDI.Gender != "NA"'.format(fam[0])).fetchall()
            childrentemp = []
            for child in children:
                c1 = []
                f1 = []
                c1.append(child[1].split())
                f1.append(fam[2].split())
                try:
                    f2 = f1[0][1]
                except IndexError:
                    f2 = 'null'
                try:
                    c2 = c1[0][1]
                except IndexError:
                    c2 = 'null'
                if f2 != c2:
                    res.append((fam[1], child[0]))
        return res
