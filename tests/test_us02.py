"""
Test for user story 02.

@author: Kipsy Quevada, pair programmed with Besnik Balaj
"""

from modules.us02 import UserStory02
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_02 = UserStory02()

def test_us02_01():
    execute_test('us02_01.ged', conn)
    assert user_story_02.get_rows(conn) == []

def test_us02_02():
    execute_test('us02_02.ged', conn)
    assert user_story_02.get_rows(conn) == [('US02_T02_I01', '3000-01-01', '2000-01-01')]

def test_us02_03():
    execute_test('us02_03.ged', conn)
    assert user_story_02.get_rows(conn) == []

def test_us02_04():
    execute_test('us02_04.ged', conn)
    assert user_story_02.get_rows(conn) == [('US02_T04_I01', '2000-01-01', '1000-01-01'), ('US02_T04_I02', '2000-01-01', '1000-01-01'), ('US02_T04_I03', '2000-01-01', '1000-01-01')]

def test_us02_05():
    execute_test('us02_05.ged', conn)
    assert user_story_02.get_rows(conn) == [('US02_T05_I03', '2000-01-01', '1000-01-01'), ('US02_T05_I04', '2000-01-01', '1000-01-01')]
