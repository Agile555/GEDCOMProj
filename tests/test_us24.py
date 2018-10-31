"""
Test for user story 24.

@author: Kipsy Quevada
"""

from modules.us24 import UserStory24
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_24 = UserStory24()

def test_us24_01():
    execute_test('us24_01.ged', conn)
    assert user_story_24.get_rows(conn) == [('US24_T01_F01', 'US24_T01_F02')]

def test_us24_02():
    execute_test('us24_02.ged', conn)
    assert user_story_24.get_rows(conn) == []

def test_us24_03():
    execute_test('us24_03.ged', conn)
    assert user_story_24.get_rows(conn) == [('US24_T03_F01', 'US24_T03_F02'), ('US24_T03_F01', 'US24_T03_F03'), ('US24_T03_F02', 'US24_T03_F03')]

def test_us24_04():
    execute_test('us24_04.ged', conn)
    assert user_story_24.get_rows(conn) == []

def test_us24_05():
    execute_test('us24_05.ged', conn)
    assert user_story_24.get_rows(conn) == []