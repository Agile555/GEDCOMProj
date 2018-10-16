"""
Test for user story 36.

@author: Michael Ameer
"""

from modules.us36 import UserStory36
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_36 = UserStory36()

def test_us36_01():
    execute_test('us36_01.ged', conn)
    assert user_story_36.get_rows(conn) == []

def test_us36_02():
    execute_test('us36_02.ged', conn)
    assert user_story_36.get_rows(conn) == [('US36_T02_I01', '2018-10-01')]

def test_us36_03():
    execute_test('us36_03.ged', conn)
    assert user_story_36.get_rows(conn) == []
