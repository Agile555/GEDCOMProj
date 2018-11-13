"""
Test for user story 42.

@author: Mark Freeman, Besnik Balaj
"""

from modules.us42 import UserStory42
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_42 = UserStory42()

#One guy born with an illegitimate date
def test_US42_01():
    execute_test('us42_01.ged', conn)
    assert user_story_42.get_rows(conn) == [('US42_T01_I01')]

def test_US42_02():
    execute_test('us42_02.ged', conn)
    assert user_story_42.get_rows(conn) == [('US42_T02_I01')]

def test_US42_03():
    execute_test('us42_03.ged', conn)
    assert user_story_42.get_rows(conn) == [('US42_T03_I01')]
