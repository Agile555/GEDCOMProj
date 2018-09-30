"""
Test for user story 08.

@author: Mark Freeman, Besnik Balaj
"""

from modules.us08 import UserStory08
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_08 = UserStory08()

#one bad entry
def test_us08_01():
    execute_test('us08_01.ged', conn)
    assert user_story_08.get_rows(conn) == [('US08_T01_I01', 'US08_T01_F01', '2000-01-01', '1990-01-01')]

#one good entry
def test_us08_02():
    execute_test('us08_02.ged', conn)
    assert user_story_08.get_rows(conn) == []

#multiple bad entries
def test_us08_03():
    execute_test('us08_03.ged', conn)
    assert user_story_08.get_rows(conn) == [('US08_T03_I01', 'US08_T03_F01', '2000-01-01', '1990-01-01'), ('US08_T03_I02', 'US08_T03_F02', '2000-01-01', '1990-01-01'), ('US08_T03_I03', 'US08_T03_F03', '2000-01-01', '1990-01-01')]

#many good entries
def test_us08_04():
    execute_test('us08_04.ged', conn)
    assert user_story_08.get_rows(conn) == []

#mix of good and bad entries
def test_us08_05():
    execute_test('us08_05.ged', conn)
    assert user_story_08.get_rows(conn) == [('US08_T05_I02', 'US08_T05_F02', '2000-01-01', '1990-01-01'), ('US08_T05_I04', 'US08_T05_F04', '2000-01-01', '1990-01-01'), ('US08_T05_I06', 'US08_T05_F06', '2000-01-01', '1990-01-01')]