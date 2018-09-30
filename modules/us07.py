import sqlite3
import datetime

def get_rows(conn):
    c = conn.cursor()
    res = []
    rows = c.execute("SELECT ID, Birthday, Death FROM INDI WHERE Age > 150 ").fetchall()
    for row in rows:
        #Check for if death occurred at least but too late
        if row[2] != 'NA':
            res.append(row)
            res.append('Y')
        else:
            res.append(row)
            res.append('N')
    return res
def US07(conn):
    list = get_row(conn)
    print_records(list)

def post_rows(list):
    #list: 0-ID, 1-Birthday, 2-Death, 3-Check
    for row in list:
        if res[3] == 'Y':
            print('ERROR: Death is greater than 150 years after Birth for ' + list[0])
        else:
            print('ERROR: Current date is not less than 150 years after Birth for' + list[0] )
