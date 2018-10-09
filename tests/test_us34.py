"""
Test for User Story 34.

@author: Besnik Balaj
"""

from modules.us34 import UserStory34
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_34 = UserStory34()

#Husband twice as old
def test_us34_01():
    execute_test('us34_01.ged', conn)
    assert user_story_34.get_rows(conn) == [('US34_T01_I01', '50', 'US34_T01_I02','10')]

#Wife twice as old
def test_us34_02():
    execute_test('us34_02.ged', conn)
    assert user_story_34.get_rows(conn) == [('US34_T02_I01', '10','US34_T02_I02','50')]

#Neither older
def test_us34_03():
    execute_test('us34_03.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T03_I01', '50','US34_T03_I02','50')]

#Multiple husband twice as old
def test_us34_04():
    execute_test('us34_04.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T04_I03', '50', 'US34_T04_I04','10'),('US34_T04_I01', '50', 'US34_T04_I02','10')]

#Multiple wife twice as old
def test_us34_05():
    execute_test('us34_05.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T05_I03', '10', 'US34_T05_I04','50'),('US34_T05_I01', '10', 'US34_T05_I02','50')]

#Mixed of old/neither
def test_us34_06():
    execute_test('us34_06.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T06_I03', '50','US34_T06_I04','10'),('US34_T06_I01', '10', 'US34_T06_I02','50')]
