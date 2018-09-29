"""
Collection of utilities to assist with general functions that were abstracted, such as resetting the database,
carrying out the execution of a test, etc.

@author: Mark Freeman
"""
from parser import parse
import sqlite3

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