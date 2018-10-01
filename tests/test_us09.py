"""
Test for user story 09.

@author: Mark Freeman
"""

from modules.us09 import UserStory09
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_09 = UserStory09()

#one family who both died after their child was born
def test_us09_01():
    execute_test('us09_01.ged', conn)
    assert user_story_09.get_rows(conn) == []

#one family whos father died 10 years before the child was born
def test_us09_02():
    execute_test('us09_02.ged', conn)
    assert user_story_09.get_rows(conn) == [('US09_T02_F01', 'US09_T02_I01', 'US09_T02_I02', 'Husband')]

#one family whos father died 1 month before their child was born
def test_us09_03():
    execute_test('us09_03.ged', conn)
    assert user_story_09.get_rows(conn) == []

#one family whos mother died before the child was born
def test_us09_04():
     execute_test('us09_04.ged', conn)
     assert user_story_09.get_rows(conn) == [('US09_T04_F01', 'US09_T04_I01', 'US09_T04_I02', 'Wife')]

#one family whos father and mother both died years before their child was born
def test_us09_05():
     execute_test('us09_05.ged', conn)
     assert user_story_09.get_rows(conn) == [('US09_T05_F01', 'US09_T05_I01', 'US09_T05_I03', 'Husband'), ('US09_T05_F01', 'US09_T05_I01', 'US09_T05_I02', 'Wife')]