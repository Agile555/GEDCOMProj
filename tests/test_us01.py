"""
Test for user story 01.

@author: Kipsy Quevada
"""

from modules.us01 import UserStory01
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_01 = UserStory01()

#one bad entry
def test_us01_01():
    execute_test('us01_01.ged', conn)
    assert user_story_01.get_rows(conn) == [('US01_T01_I01', '3000-01-01')]

#one good entry
def test_us01_02():
    execute_test('us01_02.ged', conn)
    assert user_story_01.get_rows(conn) == []

#many bad entries
def test_us01_03():
    execute_test('us01_03.ged', conn)
    assert user_story_01.get_rows(conn) == [('US01_T03_I01', '3000-01-01'), ('US01_T03_F02', '3000-01-01'), ('US01_T03_F03', '3000-01-01'), ('US01_T03_I04', '3000-01-01')]

#many good entries
def test_us01_04():
    execute_test('us01_04.ged', conn)
    assert user_story_01.get_rows(conn) == []

#mix of good and bad entries within 1 indi
def test_us01_05():
    execute_test('us01_05.ged', conn)
    assert user_story_01.get_rows(conn) == [('US01_T05_I01', '3000-01-01'), ('US01_T05_I01', '3000-01-01')]