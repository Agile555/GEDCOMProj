"""
Test for user story 34.

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
    assert user_story_34.get_rows(conn) == [('US34_T01_I01', '58', '2010-01-01','US34_T01_I02','18','2010-01-01')]

#Wife twice as old
def test_us34_02():
    execute_test('us34_02.ged', conn)
    assert user_story_34.get_rows(conn) == [('US34_T02_I01', '18', '2010-01-01','US34_T02_I02','58','2010-01-01')]

#Neither older
def test_us34_03():
    execute_test('us34_03.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T03_I01', '58', '2010-01-01','US34_T03_I02','58','2010-01-01')]

#Multiple husband twice as old
def test_us34_04():
    execute_test('us34_04.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T04_I01', '58', '2010-01-01','US34_T04_I02','18','2010-01-01'), ('US34_T04_I03', '58', '2010-01-01','US34_T04_I04','18','2010-01-01')]

#Multiple wife twice as old
def test_us34_05():
    execute_test('us34_05.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T05_I01', '18', '2010-01-01','US34_T05_I02','58','2010-01-01'), ('US34_T05_I03', '18', '2010-01-01','US34_T05_I04','58','2010-01-01')]

#Mixed of old/neither
def test_us34_06():
    execute_test('us34_06.ged',conn)
    assert user_story_34.get_rows(conn) == [('US34_T06_I01', '18', '2010-01-01','US34_T06_I02','58','2010-01-01'), ('US34_T06_I03', '58', '2010-01-01','US34_T06_I04','18','2010-01-01')]
