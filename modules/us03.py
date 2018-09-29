"""
User story 03 prints an error if any individuals of the database are found to have a birth
data that occurs after they have died.

@author: Mark Freeman
"""

from datetime import datetime

def print_rows(rows):
    for row in rows:
        print('ERROR: Birthday on ' + lst[1] + ' occurs after death on ' + lst[2] + ' for user ' + lst[0])

def get_rows(conn):
    c = conn.cursor()
    res = []
    rows = c.execute('SELECT ID, Birthday, Death FROM INDI WHERE Birthday != "NA" AND Death != "NA"').fetchall()
    for row in rows:
        if(datetime.strptime(row[1], '%Y-%m-%d') > datetime.strptime(row[2], '%Y-%m-%d')): #get the birth and death and compare dates
            res.append(row)
    return res

#use same megatron connection for all use cases called from index.py
def us03(conn):
    rows = get_rows(conn)
    print_rows(rows)