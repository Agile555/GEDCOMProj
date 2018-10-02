"""
Test for user story 29.

@author: Michael Ameer
"""

from modules.us29 import UserStory29
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_29 = UserStory29()

def test_us29_01():
    execute_test('us29_01.ged', conn)
    assert user_story_29.get_rows(conn) == []

def test_us29_02():
    execute_test('us29_02.ged', conn)
    assert user_story_29.get_rows(conn) == [('US29_T02_I01', )]

def test_us29_03():
    execute_test('us29_03.ged', conn)
    assert user_story_29.get_rows(conn) == [('US29_T03_I01', ),('US29_T03_I02', )] #these must be tuples

def test_us29_04():
    execute_test('us29_04.ged', conn)
    assert user_story_29.get_rows(conn) == []

def test_us29_05():
    execute_test('us29_05.ged', conn)
    assert user_story_29.get_rows(conn) == []

