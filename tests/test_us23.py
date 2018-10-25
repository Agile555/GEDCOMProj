"""
Test for user story 23.
@author: Michael Ameer
"""

from modules.us23 import UserStory23
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_23 = UserStory23()

def test_us23_01():
    execute_test('us23_01.ged', conn)
    assert user_story_23.get_rows(conn) == [('US23_T01_I01', 'US23_T01_I02')]

def test_us23_02():
    execute_test('us23_02.ged', conn)
    assert user_story_23.get_rows(conn) == []

def test_us23_03():
    execute_test('us23_03.ged', conn)
    assert user_story_23.get_rows(conn) == []

def test_us23_04():
    execute_test('us23_04.ged', conn)
    assert user_story_23.get_rows(conn) == [('US23_T04_I01', 'US23_T04_I02'), ('US23_T04_I01', 'US23_T04_I03'), ('US23_T04_I02', 'US23_T04_I03')]

def test_us23_05():
    execute_test('us23_05.ged', conn)
    assert user_story_23.get_rows(conn) == []
