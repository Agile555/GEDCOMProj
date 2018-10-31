"""
Test for user story 16.
@author: Michael Ameer
"""

from modules.us16 import UserStory16
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_16 = UserStory16()

def test_us16_01():
    execute_test('us16_01.ged', conn)
    assert user_story_16.get_rows(conn) == [('US16_T01_I01', 'US16_T01_I02')]

def test_us16_02():
    execute_test('us16_02.ged', conn)
    assert user_story_16.get_rows(conn) == []

def test_us16_03():
    execute_test('us16_03.ged', conn)
    assert user_story_16.get_rows(conn) == [('US16_T03_I01', 'US16_T03_I02')]

def test_us16_04():
    execute_test('us16_04.ged', conn)
    assert user_story_16.get_rows(conn) == [('US16_T04_I01', 'US16_T04_I02'), ('US16_T04_I01', 'US16_T04_I04')]

def test_us16_05():
    execute_test('us16_05.ged', conn)
    assert user_story_16.get_rows(conn) == [('US16_T05_I01', 'US16_T05_I02'), ('US16_T05_I01', 'US16_T05_I04')]
