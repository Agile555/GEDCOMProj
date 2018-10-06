"""
Test for user story 18.

@author: Mark Freeman
"""

from modules.us18 import UserStory18
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_18 = UserStory18()

#one family where siblings married each other
def test_us18_01():
    execute_test('us18_01.ged', conn)
    assert user_story_18.get_rows(conn) == [('US18_T01_F02', 'US18_T01_I01', 'US18_T01_I02')]

#one family whose siblings married other people
def test_us18_02():
    execute_test('us18_02.ged', conn)
    assert user_story_18.get_rows(conn) == []

#one family where siblings married each other, but they weren't the only children in the family
def test_us18_03():
    execute_test('us18_03.ged', conn)
    assert user_story_18.get_rows(conn) == [('US18_T03_F02', 'US18_T03_I02', 'US18_T03_I03')]