"""
Test for user story 05.

@author: Mark Freeman
"""

from modules.us05 import UserStory05
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_05 = UserStory05()

#one bad entry
def test_us05_01():
    execute_test('us05_01.ged', conn)
    assert user_story_05.get_rows(conn) == [('US05_T01_I01', '2000-01-01', '1990-01-01')]

#one good entry
def test_us05_02():
    execute_test('us05_02.ged', conn)
    assert user_story_05.get_rows(conn) == []

#multiple bad entries
def test_us05_03():
    execute_test('us05_03.ged', conn)
    assert user_story_05.get_rows(conn) == [('US05_T03_I01', '2000-01-01', '1990-01-01'), ('US05_T03_I02', '2000-01-01', '1990-01-01'), ('US05_T03_I03', '2000-01-01', '1990-01-01')]

#multiple good entries
def test_us05_04():
    execute_test('us05_04.ged', conn)
    assert user_story_05.get_rows(conn) == []

#mix of good and bad entries
def test_us05_05():
    execute_test('us05_05.ged', conn)
    assert user_story_05.get_rows(conn) == [('US05_T05_I02', '2000-01-01', '1990-01-01'), ('US05_T05_I04', '2000-01-01', '1990-01-01'), ('US05_T05_I06', '2000-01-01', '1990-01-01')]