"""
Test for User Story 10.

@author: Besnik Balaj
"""

from modules.us10 import UserStory10
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_10 = UserStory10()

#Wife was not 14 years of age
def test_us10_01():
    execute_test('us10_01.ged', conn)
    assert user_story_10.get_rows(conn) == [('US10_T01_I01', '50', 'US10_T01_I02','10')]

#2 wives were not of 14 years of age
def test_us10_02():
    execute_test('us10_02.ged', conn)
    assert user_story_10.get_rows(conn) == [('US10_T02_I01', '50', 'US10_T02_I02','10'),('US10_T02_I03', '50', 'US10_T02_I04','10')]

#Husband was not 14 years of Age
def test_us10_03():
    execute_test('us10_03.ged', conn)
    assert user_story_10.get_rows(conn) == [('US10_T03_I01', '10', 'US10_T03_I02','50')]

#2 Husbands were not of 14 years of age
def test_us10_04():
    execute_test('us10_04.ged', conn)
    assert user_story_10.get_rows(conn) == [('US10_T04_I01', '10', 'US10_T04_I02','50'),('US10_T04_I03', '10', 'US10_T04_I04','50')]

#Mix of husband and wife being not of age
def test_us10_05():
    execute_test('us10_05.ged', conn)
    assert user_story_10.get_rows(conn) == [('US10_T05_I01', '50', 'US10_T05_I02','9'),('US10_T05_I03', '9', 'US10_T05_I04','50')]

#One extra husband
def test_us10_06():
    execute_test('us10_06.ged', conn)
    assert user_story_10.get_rows(conn) == [('US10_T06_I01', '10', 'US10_T06_I02', '50')]

#Family was stated but not filled with husband or wife
def test_us10_07():
    execute_test('us10_07.ged', conn)
    assert user_story_10.get_rows(conn) == []
