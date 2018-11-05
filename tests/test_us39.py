"""
Test for user story 39.

@author: Mark Freeman
"""

from modules.us39 import UserStory39
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_39 = UserStory39()

#one family who has an upcoming anniversary at the time of this writing
def test_us39_01():
    execute_test('us39_01.ged', conn)
    assert user_story_39.get_rows(conn) == [('US39_T01_F01', '2000-12-05')]

#one family whos anniversary is farther away
def test_us39_02():
    execute_test('us39_02.ged', conn)
    assert user_story_39.get_rows(conn) == []

#family who has upcoming marraige but one of them is dead
def test_us39_03():
    execute_test('us39_03.ged', conn)
    assert user_story_39.get_rows(conn) == []

#family with upcoming marriage but both are dead
def test_us39_04():
    execute_test('us39_04.ged', conn)
    assert user_story_39.get_rows(conn) == []

#family who divorced but would otherwise have an upcoming marriage
def test_us39_05():
    execute_test('us39_05.ged', conn)
    assert user_story_39.get_rows(conn) == []

#family who has an anniversary that just passed at the time of this writing
def test_us39_06():
    execute_test('us39_06.ged', conn)
    assert user_story_39.get_rows(conn) == []
