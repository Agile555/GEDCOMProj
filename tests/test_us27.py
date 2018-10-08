from modules.us27 import UserStory27
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_27 = UserStory27()

#insert some people of different ages who have died
def test_us27_01():
    execute_test('us27_01.ged', conn)
    assert user_story_27.get_rows(conn) == [('10', )]

#insert one person who died on a day other than his birthday
def test_us27_02():
    execute_test('us27_02.ged', conn)
    assert user_story_27.get_rows(conn) == [('20', )]

#insert a couple of people
def test_us27_03():
    execute_test('us27_03.ged', conn)
    assert user_story_27.get_rows(conn) == [('10', ), ('20', )]