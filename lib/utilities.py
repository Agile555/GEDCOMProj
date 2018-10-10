"""
Collection of utilities to assist with general functions that were abstracted, such as resetting the database,
carrying out the execution of a test, etc.

@author: Mark Freeman
"""
from lib.parser import parse
from datetime import datetime, timedelta
import sqlite3

time_units = {"days": 1, "weeks": 7, "months": 30.44, "years": 365.25}

def reset_db(conn):
    """
    Reset the tables in a database and set up necessary structure.  Important to occur between tests if we have a single connection.

    Args:
        conn (connection): an SQLite connection object which represents the database
            we plan on writing information to

    Returns:
        None
    """
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS INDI")
    c.execute("DROP TABLE IF EXISTS FAM")
    c.execute("DROP TABLE IF EXISTS CHLD")
    c.execute("CREATE TABLE INDI(ID TEXT PRIMARY KEY, Name TEXT, Gender TEXT, Birthday TEXT, Age TEXT, Alive TEXT, Death TEXT, Child TEXT, Spouse TEXT)")
    c.execute("CREATE TABLE FAM(ID TEXT PRIMARY KEY, Married TEXT, Divorced TEXT, 'Husband ID' TEXT, 'Husband Name' TEXT, 'Wife ID' TEXT, 'Wife Name' TEXT, Children TEXT)")
    c.execute("CREATE TABLE CHLD(FAM_ID TEXT, INDI_ID TEXT)")
    conn.commit()

def execute_test(test_name, conn):
    """
    Carry out the execution of a test.  This involves setting up a fresh database to interact with and parsing the target file

    Args:
        test_name (string): name of the .ged file in the ged directory which we are going to test
        conn (connection): an SQLite connection object which represents the database
            we plan on writing information to

    Returns:
        None
    """
    reset_db(conn)
    parse('./ged/' + test_name, conn)

def fill_megatron(test_name):
    """
    Fill the megatron database directly with the supplied ged file.  Useful for inspecting a database after parsing and for
    running SQL commands directly against a parsed file, perhaps for testing to generate a get_rows function.

    Args:
        test_name (string): the name of the ged file inside of the ged directory to parse

    Returns:
        None
    """
    conn = sqlite3.connect('megatron.db')
    execute_test(test_name, conn)

def is_in_range(d, d_start, length, unit='days'):
    """
    Determine if a date falls within a given range after a certain date.

    Args:
        d (datetime): a datetime object representing the date we are checking
        d_start (datetime): a datetime object representing the start of the range we wish to check
        length (int): the number of units we are extending the start date by to get our range
        unit (string): a string representing the unit of time (days || weeks || months || years) 

    Returns:
        (bool): the date falls within the range
    """
    if(d < d_start or d > d_start + timedelta(days = length * time_units[unit])):
        return False
    return True

#TODO: work on documentation
def is_upcoming(d, d_start, length, unit):
    """
    Determine if a date is within an upcoming range, regardless of the year. (e.g. birthday, anniversary, holiday)

    Args:
        d (datetime): a datetime object representing the date we are checking (usually today)
        d_start (datetime): a datetime object representing the start of the range we wish to check (usually a birthday, anniversary, holiday, etc.)
        length (int): the number of units we are extending the start date by to get our range
        unit (string): a string representing the unit of time (days || weeks || months || years) 

    Returns:
        (bool): date is within the range on the month and day regardless of year
    """
    return ((d_start - d) % timedelta(days=365.25)).days <= length * time_units[unit] #we assume the date we are checking is most recent    

def fast_forward(d, length, unit):
    """
    Fast forward a date a specified period of time

    Args:
        d (datetime): a datetime object representing the date to move forward from
        length (int): the number of units we are extending the start date by
        unit (string): a string representing the unit of time (days || weeks || months || years)

    Returns:
        (datetime): a date reflecting the appropriate amount of time moved forward from the given date
    """
    return d + timedelta(days = length * time_units[unit])

def rewind(d, length, unit):
    """
    Rewinds a date a specified period of time. (Same as fast forward function, just in reverse)

    Args:
        d (datetime): a datetime object representing the date to move forward from
        length (int): the number of units we are extending the start date by
        unit (string): a string representing the unit of time (days || weeks || months || years)

    Returns:
        (datetime): a date reflecting the appropriate amount of time moved forward from the given dates
    """
    return d + timedelta(days = length * time_units[unit])

def get_years(delta):
    """
    Retrieve the years from a timedelta object.

    Args:
        delta (timedelta): the timedelta object to pull years from

    Returns:
        (int): the floored years passed in the timedelta object
    """
    return int(delta.days // time_units['years'])

def parse_string(d):
    """
    Parse a string from a year-month-day format to get a datetime object

    Args:
        d (string): a string that we wish to parse

    Returns:
        (datetime): a datetime object representing the parsed time
    """
    return datetime.strptime(d, '%Y-%m-%d')

def format_date(d):
    """
    Format a datetime object into a string

    Args:
        d (datetime): a datetime object we wish to format
    
    Returns:
        (string): a string representing our datetime object
    """
    return datetime.strftime(d, '%Y-%m-%d')