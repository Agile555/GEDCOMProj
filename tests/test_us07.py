"""
Test for user story 07.

@author: Besnik Balaj
"""

from modules.us07 import UserStory07
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_07 = UserStory07()

def test_us07_01():
    execute_test('us07_01.ged', conn)
    assert user_story_07.get_rows(conn) == [('US07_T01_I01', 'NA', '219')]

def test_us07_02():
    execute_test('us07_02.ged', conn)
    assert user_story_07.get_rows(conn) == []

def test_us07_03():
    execute_test('us07_03.ged', conn)
    assert user_story_07.get_rows(conn) == [('US07_T03_I01', '2000-01-01','200')]

def test_us07_04():
    execute_test('us07_04.ged', conn)
    assert user_story_07.get_rows(conn) == [('US07_T04_I01', 'NA','219'),('US07_T04_I02', 'NA','198')]
