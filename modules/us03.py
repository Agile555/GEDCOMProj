import sqlite3
import datetime

def print_rows(lst):
    for row in lst:
        print('ERROR: Birthday ' + lst[1] + ' occurs after death ' + lst[2] + ' for user ' + lst[0])

def get_rows(conn):
    c = conn.cursor()
    res = []
    rows = c.execute('SELECT ID, Birthday, Death FROM INDI WHERE Birthday != "NA" AND Death != "NA"').fetchall()
    for row in rows:
        if(datetime.datetime.strptime(row[1], '%Y-%m-%d') > datetime.datetime.strptime(row[2], '%Y-%m-%d')): #get the birth and death and compare dates
            res.append(row)
    return res

#use same megatron connection for all use cases called from index.py
def us03(conn):
    lst = get_rows(conn)
    print_rows(lst)