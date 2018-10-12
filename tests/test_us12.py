"""
Test for user story 12.

@author: Kipsy Quevada, Besnik Balaj
"""

from modules.us12 import UserStory12
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_12 = UserStory12()

def test_us12_01():
    execute_test('us12_01.ged', conn)
    assert user_story_12.get_rows(conn) == [('US12_T01_I02', 'US12_T01_I03'), ('US12_T01_I01', 'US12_T01_I04'), ('US12_T01_I02', 'US12_T01_I04')]

def test_us12_12():
    execute_test('us12_02.ged', conn)
    assert user_story_12.get_rows(conn) == []

def test_us12_03():
    execute_test('us12_03.ged', conn)
    assert user_story_12.get_rows(conn) == [('US12_T01_I02', 'US12_T01_I03')]

def test_us12_04():
    execute_test('us12_04.ged', conn)
    assert user_story_12.get_rows(conn) == [('US12_T01_I02', 'US12_T01_I03'), ('US12_T01_I02', 'US12_T01_I04'), ('US12_T01_I02', 'US12_T01_I05')]

def test_us12_05():
    execute_test('us12_05.ged', conn)
    assert user_story_12.get_rows(conn) == []
