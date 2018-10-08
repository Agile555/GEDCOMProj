"""
Test for user story 32.

@author: Mark Freeman
"""

from modules.us32 import UserStory32
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_32 = UserStory32()

#Insert a family with five children all born on the same day
def test_us32_01():
    execute_test('us32_01.ged', conn)
    assert user_story_32.get_rows(conn) == [('US32_T01_F01', ['1990-01-01'])]

#Insert a family with five children.  One of them was born on the next day, as the delivery occurred at 11:59 PM for the fourth child and 12:01 AM for fifth
def test_us32_02():
    execute_test('us32_02.ged', conn)
    assert user_story_32.get_rows(conn) == [('US32_T02_F01', ['1990-01-01', '1990-01-02'])]

#Insert a family with five children.  Three of them was born on the next day, as the delivery occurred at 11:59 PM for the second child and 12:01 AM for third
def test_us32_03():
    execute_test('us32_03.ged', conn)
    assert user_story_32.get_rows(conn) == [('US32_T03_F01', ['1990-01-01', '1990-01-02'])]

#Insert a family with five children, however we know nothing about when they were born
def test_us32_04():
    execute_test('us32_04.ged', conn)
    assert user_story_32.get_rows(conn) == []

#Insert a family with six children, half of them born 10 years apart
def test_us32_05():
    execute_test('us32_05.ged', conn)
    assert user_story_32.get_rows(conn) == []

#Insert a family with five children, each born one day apart
def test_us32_06():
    execute_test('us32_06.ged', conn)
    assert user_story_32.get_rows(conn) == []