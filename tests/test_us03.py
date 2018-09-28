from modules.us03 import get_rows
from parser import main
from utilities import reset_db
import sqlite3

conn = sqlite3.connect(':memory:')

#All good entries
def test_us03_1():
    reset_db(conn)
    main('./ged/us03_01.ged', conn)
    assert get_rows(conn) == []

# #Single bad entry
# def test_us03_2():
#     assert get_rows('/home/mark/Desktop/school/fall2018/ssw-555/proj/GEDCOMProj/dbs/us03_2.db') == [('I11', '1960-01-01', '1950-01-01')]

# #Multi bad entry
# def test_us03_3():
#     assert get_rows('/home/mark/Desktop/school/fall2018/ssw-555/proj/GEDCOMProj/dbs/us03_3.db') == [('I11', '1960-01-01', '1950-01-01'),('I13', '1980-01-01', '1910-01-01')]

# #Multi bad entry with missing birthday
# def test_us03_4():
#     assert get_rows('/home/mark/Desktop/school/fall2018/ssw-555/proj/GEDCOMProj/dbs/us03_4.db') == [('I11', '1960-01-01', '1950-01-01'),('I13', '1980-01-01', '1910-01-01')]

# #Never born or dead
# def test_us03_5():
#     assert get_rows('/home/mark/Desktop/school/fall2018/ssw-555/proj/GEDCOMProj/dbs/us03_5.db') == []

# def test_us03_4():
#     assert get_rows('../temp.db') == [] #we are allowed to go one level out, this gives me an idea...
# perhaps a temporary testing db that we inflate and destroy as we test? This way we write GEDCOM involving the parser and only have
# .ged testing files instead of db files