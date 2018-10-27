from modules.us28 import UserStory28
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_28 = UserStory28()

#insert some children
def test_us28_01():
    execute_test('us28_01.ged', conn)
    assert user_story_28.get_rows(conn) == ['US28_T01_I01 (28), US28_T01_I02 (27)']

#insert one child
def test_us28_02():
    execute_test('us28_02.ged', conn)
    assert user_story_28.get_rows(conn) == ['US28_T02_I01 (28)']

#insert some children in two families
def test_us28_03():
    execute_test('us28_03.ged', conn)
    assert user_story_28.get_rows(conn) == ['US28_T03_I01 (28), US28_T03_I02 (27)', 'US28_T03_I03 (28), US28_T03_I04 (27)']

#insert no children
def test_us28_04():
    execute_test('us28_04.ged', conn)
    assert user_story_28.get_rows(conn) == ['']

#insert no children (they are parents)
def test_us28_05():
    execute_test('us28_05.ged', conn)
    assert user_story_28.get_rows(conn) == ['']