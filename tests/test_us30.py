"""
Test for user story 30.

@author: Kipsy Quevada
"""

from modules.us30 import UserStory30
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_30 = UserStory30()

def test_us30_01():
    execute_test('us30_01.ged', conn)
    assert user_story_30.get_rows(conn) == []

def test_us30_02():
    execute_test('us30_02.ged', conn)
    assert user_story_30.get_rows(conn) == [('US30_T02_I01', )]

def test_us30_03():
    execute_test('us30_03.ged', conn)
    assert user_story_30.get_rows(conn) == [('US30_T03_I01', ),('US30_T03_I02', )]

def test_us30_04():
    execute_test('us30_04.ged', conn)
    assert user_story_30.get_rows(conn) == []

def test_us30_05():
    execute_test('us30_05.ged', conn)
    assert user_story_30.get_rows(conn) == []

