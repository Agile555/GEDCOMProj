from modules.us28 import UserStory28
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_28 = UserStory28()

#insert some children
def test_us28_01():
    execute_test('us28_01.ged', conn)
    assert user_story_28.get_rows(conn) == ['US28_T01_I01 (28),US28_T01_I02 (27)']

# #insert one person who died on a day other than his birthday
# def test_us28_02():
#     execute_test('us28_02.ged', conn)
#     assert user_story_28.get_rows(conn) == [('20', )]

# #insert a couple of people
# def test_us28_03():
#     execute_test('us28_03.ged', conn)
#     assert user_story_28.get_rows(conn) == [('10', ), ('20', )]