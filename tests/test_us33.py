"""
Test for user story 33.

@author: Mark Freeman
"""

from modules.us33 import UserStory33
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_33 = UserStory33()

#one orphaned child
def test_us33_01():
    execute_test('us33_01.ged', conn)
    assert user_story_33.get_rows(conn) == [('US33_T01_I01', '10')]

#one child whose father died when young, but his mother's death is unknown
def test_us33_02():
    execute_test('us33_02.ged', conn)
    assert user_story_33.get_rows(conn) == []

#one child whose parents both died when he was over 18
def test_us33_03():
    execute_test('us33_03.ged', conn)
    assert user_story_33.get_rows(conn) == []

#one child whose parents we do not know the death date of
def test_us33_04():
    execute_test('us33_04.ged', conn)
    assert user_story_33.get_rows(conn) == []

#one child who we do not know the birthday of, but whose parents are both dead 
def test_us33_05():
    execute_test('us33_05.ged', conn)
    assert user_story_33.get_rows(conn) == []

#one child who died very young, but whose parents went on to live for a while (not an orphan)
def test_us33_06():
    execute_test('us33_06.ged', conn)
    assert user_story_33.get_rows(conn) == []

#one orphaned child whose parents died at different times, mainly checking the age he was orphaned at
def test_us33_07():
    execute_test('us33_07.ged', conn)
    assert user_story_33.get_rows(conn) == [('US33_T07_I01', '10')]
