"""
User story 05 prints an error if any individuals are found to have gotten married after their death.

@author: Mark Freeman
"""

from datetime import datetime

def print_rows(lst):
    for row in lst:
        print('ERROR: Marriage on ' + row[1] + ' occurs after death on ' + row[2] + ' for user ' + row[0])

def get_rows(conn):
    c = conn.cursor()
    res = []
    
    #grab all records where we have a spouse that has both died and been married
    rows = c.execute('SELECT INDI.ID, Married, Death FROM FAM LEFT JOIN INDI ON (FAM."Husband ID" = INDI.ID OR FAM."Wife ID" = INDI.ID) WHERE Death != "NA"').fetchall()
    for row in rows:
        if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #if marriage after death
            res.append(row)
    return res

#use same megatron connection for all use cases called from index.py
def us05(conn):
    rows = get_rows(conn)
    print_rows(rows)