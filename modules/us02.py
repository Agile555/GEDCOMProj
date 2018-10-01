"""
User story 02 prints an error if any individuals of the database are found to have a birth
data that occurs after they were married.

@author: Kipsy Quevada, pair programmed with Besnik Balaj
"""

from datetime import datetime

def print_rows(rows):
    for row in rows:
        print('ERROR: Birthday on ' + lst[1] + ' occurs after marriage on ' + lst[2] + ' for user ' + lst[0])

def get_rows(conn):
    c = conn.cursor()
    res = []
    rows = c.execute('SELECT INDI.ID, Birthday, Married FROM FAM INNER JOIN INDI ON (FAM."Husband ID" = INDI.ID OR FAM."Wife ID" = INDI.ID) WHERE Birthday != "NA" AND Married != "NA"').fetchall()
    for row in rows:
        if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #get the birth and marriage and compare dates
            res.append(row)
    return res

#use same megatron connection for all use cases called from index.py
def us02(conn):
    rows = get_rows(conn)
    print_rows(rows)