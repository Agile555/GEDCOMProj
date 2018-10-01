"""
Test for user story 31.

@author: Michael Ameer
"""

from modules.us31 import UserStory31
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_31 = UserStory31()

def test_us31_01():
    execute_test('us31_01.ged', conn)
    assert user_story_31.get_rows(conn) == [('US31_T01_I01', '58')]

def test_us31_02():
    execute_test('us31_02.ged', conn)
    assert user_story_31.get_rows(conn) == [('US31_T02_I01', '58'),('US31_T02_I02', '58')]

def test_us31_03():
    execute_test('us31_03.ged', conn)
    assert user_story_31.get_rows(conn) == []

def test_us31_04():
    execute_test('us31_04.ged', conn)
    assert user_story_31.get_rows(conn) == []

def test_us31_05():
    execute_test('us31_05.ged', conn)
    assert user_story_31.get_rows(conn) == []

