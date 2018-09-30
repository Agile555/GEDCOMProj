import sqlite3
from modules.us07 import get_rows
from utilities import execute_test


conn = sqlite3.connect(':memory:')

def test_AllPass(): #Nothing in here exceeds 150 years of age
    execute_test('us07_01.ged', conn)
    assert get_rows(conn) == []
