"""
Test for user story 41.

@author: Mark Freeman, Besnik Balaj
"""

from modules.us41 import UserStory41
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_41 = UserStory41()

#day, month, and year
def test_US41_01():
    execute_test('us41_01.ged', conn)
    assert user_story_41.get_rows(conn) == [('1990-01-01')]

#only month, year
def test_US41_02():
    execute_test('us41_02.ged', conn)
    assert user_story_41.get_rows(conn) == [('1990-01-01')]

#only year
def test_US41_03():
    execute_test('us41_03.ged', conn)
    assert user_story_41.get_rows(conn) == [('1990-01-01')]
