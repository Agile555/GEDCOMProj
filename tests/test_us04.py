"""
Test for user story 04.

@author: Mark Freeman
"""

from modules.us04 import UserStory04
from utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_04 = UserStory04()

#one bad entry
def test_us04_01():
    execute_test('us04_01.ged', conn)
    assert user_story_04.get_rows(conn) == [('US04_T01_F01', '2000-01-01', '1990-01-01')]

#one good entry
def test_us_04_02():
    execute_test('us04_02.ged', conn)
    assert user_story_04.get_rows(conn) == []

#many bad entries
def test_us_04_03():
    execute_test('us04_03.ged', conn)
    assert user_story_04.get_rows(conn) == [('US04_T03_F01', '2000-01-01', '1990-01-01'), ('US04_T03_F02', '2000-01-01', '1990-01-01'), ('US04_T03_F03', '2000-01-01', '1990-01-01')]

#many good entries
def test_us_04_04():
    execute_test('us04_04.ged', conn)
    assert user_story_04.get_rows(conn) == []

#mix of good and bad entries
def test_us_04_05():
    execute_test('us04_05.ged', conn)
    assert user_story_04.get_rows(conn) == [('US04_T05_F02', '2000-01-01', '1990-01-01'), ('US04_T05_F04', '2000-01-01', '1990-01-01'), ('US04_T05_F06', '2000-01-01', '1990-01-01')]
