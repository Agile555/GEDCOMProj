"""
Test for user story 19.

@author: Mark Freeman
"""

from modules.us19 import UserStory19
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect('megatron.db')
user_story_19 = UserStory19()

#insert one family where the husband and wife are first cousins.  The father of the husband and wife are brothers
def test_us19_01():
    execute_test('us19_01.ged', conn)
    assert user_story_19.get_rows(conn) == [('US19_T01_F01', 'US19_T01_I01', 'US19_T01_I02'), ]

#insert one family where the husband and wife are first cousins.  The mother of the husband and wife are sisters
def test_us19_02():
    execute_test('us19_02.ged', conn)
    assert user_story_19.get_rows(conn) == [('US19_T02_F01', 'US19_T02_I01', 'US19_T02_I02'), ]

#insert one family where the husband and wife are first cousins.  The father of the husband and mother of the wife are siblings
def test_us19_03():
    execute_test('us19_03.ged', conn)
    assert user_story_19.get_rows(conn) == [('US19_T03_F01', 'US19_T03_I01', 'US19_T03_I02'), ]

#insert one normal family
def test_us19_04():
    execute_test('us19_04.ged', conn)
    assert user_story_19.get_rows(conn) == []

#insert one normal family
def test_us19_05():
    execute_test('us19_05.ged', conn)
    assert user_story_19.get_rows(conn) == []

#insert a large tree of families
def test_us19_06():
    execute_test('us19_06.ged', conn)
    assert user_story_19.get_rows(conn) == []