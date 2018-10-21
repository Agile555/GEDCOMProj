"""
Test for user story 2.

@author: Besnik Balaj
"""

from modules.us21 import UserStory21
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_21 = UserStory21()

#Husband is incorrect role
def test_us21_01():
    execute_test('us21_01.ged', conn)
    assert user_story_21.get_rows(conn) == [("F","US21_T01_I01")]

#Wife is incorrect role
def test_us21_02():
    execute_test('us21_02.ged', conn)
    assert user_story_21.get_rows(conn) == [("M","US21_T02_I02")]

#Both couples are correct role
def test_us21_03():
    execute_test('us21_03.ged', conn)
    assert user_story_21.get_rows(conn) == []

#Both couples are incorrect gender
def test_us21_04():
    execute_test('us21_04.ged', conn)
    assert user_story_21.get_rows(conn) == [("F","US21_T04_I01"),("M","US21_T04_I02")]

#Multiple couples inserted where
def test_us21_05():
    execute_test('us21_05.ged', conn)
    assert user_story_21.get_rows(conn) == [("F","US21_T05_I01"),("M","US21_T05_I04")]
