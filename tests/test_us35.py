"""
Test for user story 35.

@author: Michael Ameer
"""

from modules.us35 import UserStory35
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_35 = UserStory35()

def test_us35_01():
    execute_test('us35_01.ged', conn)
    assert user_story_35.get_rows(conn) == []

def test_us35_02():
    execute_test('us35_02.ged', conn)
    assert user_story_35.get_rows(conn) == [('US35_T02_I01', '2018-11-01', '0')]

def test_us35_03():
    execute_test('us35_03.ged', conn)
    assert user_story_35.get_rows(conn) == []
