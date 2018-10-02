"""
Test for user story 03.

@author: Mark Freeman
"""

from modules.us03 import UserStory03
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_03 = UserStory03()

def test_us03_01():
    execute_test('us03_01.ged', conn)
    assert user_story_03.get_rows(conn) == []

def test_us03_02():
    execute_test('us03_02.ged', conn)
    assert user_story_03.get_rows(conn) == [('US03_T02_I01', '2000-01-01', '1990-01-01')]

def test_us03_03():
    execute_test('us03_03.ged', conn)
    assert user_story_03.get_rows(conn) == [('US03_T03_I01', '2000-01-01', '1990-01-01'), ('US03_T03_I02', '2000-01-01', '1990-01-01'), ('US03_T03_I03', '2000-01-01', '1990-01-01')]

def test_us03_04():
    execute_test('us03_04.ged', conn)
    assert user_story_03.get_rows(conn) == []

def test_us03_05():
    execute_test('us03_05.ged', conn)
    assert user_story_03.get_rows(conn) == [('US03_T05_I02', '2000-01-01', '1990-01-01'), ('US03_T05_I04', '2000-01-01', '1990-01-01')]
