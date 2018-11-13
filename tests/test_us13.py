"""
Test for User Story 13

@author: Mark Freeman
"""

from modules.us13 import UserStory13
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_13 = UserStory13()

def test_us13_01():
    execute_test('us13_01.ged', conn)
    assert user_story_13.get_rows(conn) == []

def test_us13_02():
    execute_test('us13_02.ged', conn)
    assert user_story_13.get_rows(conn) == []

def test_us13_03():
    execute_test('us13_03.ged', conn)
    assert user_story_13.get_rows(conn) == [('US13_T03_F01', 'US13_T03_I01', 'US13_T03_I02', '1990-01-01', '1990-01-03')]

def test_us13_04():
    execute_test('us13_04.ged', conn)
    assert user_story_13.get_rows(conn) == [('US13_T04_F01', 'US13_T04_I01', 'US13_T04_I02', '1990-01-01', '1990-03-01'), ('US13_T04_F01', 'US13_T04_I01', 'US13_T04_I03', '1990-01-01', '1990-05-01'), ('US13_T04_F01', 'US13_T04_I02', 'US13_T04_I03', '1990-03-01', '1990-05-01')]

def test_us13_05():
    execute_test('us13_05.ged', conn)
    assert user_story_13.get_rows(conn) == []