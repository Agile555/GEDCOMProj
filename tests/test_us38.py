"""
Test for user story 38.

@author: Mark Freeman
"""

from modules.us38 import UserStory38
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_38 = UserStory38()

#one user who died in the past
def test_us38_01():
    execute_test('us38_01.ged', conn)
    assert user_story_38.get_rows(conn) == []

#one user whose birthday is coming up at the time of writing this
def test_us38_02():
    execute_test('us38_02.ged', conn)
    assert user_story_38.get_rows(conn) == [('US38_T02_I01', '2000-11-05')]

#one user whose birthday is farther out at the time of writing this
def test_us38_03():
    execute_test('us38_03.ged', conn)
    assert user_story_38.get_rows(conn) == []

#one user whose birthday just passed at the time of writing this
def test_us38_04():
    execute_test('us38_04.ged', conn)
    assert user_story_38.get_rows(conn) == []

def test_us38_05():
    execute_test('us38_05.ged', conn)
    assert user_story_38.get_rows(conn) == [('US38_T05_I01', '2000-11-01')]