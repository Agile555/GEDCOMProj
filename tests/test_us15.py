"""
Test for User Story 15.

@author: Besnik Balaj
"""

from modules.us15 import UserStory15
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_15 = UserStory15()

#Family has 15 siblings
def test_us15_01():
    execute_test('us15_01.ged', conn)
    assert user_story_15.get_rows(conn) == []

#Family has less than 15 siblings
def test_us15_02():
    execute_test('us15_02.ged',conn)
    assert user_story_15.get_rows(conn) == []

#Family has more than 15 siblings
def test_us15_03():
    execute_test('us15_03.ged',conn)
    assert user_story_15.get_rows(conn) == [("US15_T03_F01")]

#Family with no kids
def test_us15_04():
    execute_test('us15_04.ged',conn)
    assert user_story_15.get_rows(conn) == []

#2 families where 1 fails and 1 passes
def test_us15_05():
    execute_test('us15_05.ged',conn)
    assert user_story_15.get_rows(conn) == [("US15_T05_F01")]
