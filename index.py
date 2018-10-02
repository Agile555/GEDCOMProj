"""
Entry point for GEDCOM parsing application.

@author: Mark Freeman, Michael Ameer, Besnik Balaj, Kipsy Quevada
"""

from modules import us01, us02, us03, us04, us05, us06, us07, us08, us09, us29, us31, us33, us41
from lib.utilities import reset_db, execute_test
import sqlite3

def main():
    #set up the database
    conn = sqlite3.connect('megatron.db')
    reset_db(conn)

    #fill the database with our entire test suite as one file
    #command is `cat * > optimus_prime.ged`
    execute_test('optimus_prime.ged', conn)

    #instantiate all of our tests and fire them
    stories = []
    stories.append(us01.UserStory01())
    stories.append(us02.UserStory02())
    stories.append(us03.UserStory03())
    stories.append(us04.UserStory04())
    stories.append(us05.UserStory05())
    stories.append(us06.UserStory06())
    stories.append(us07.UserStory07())
    stories.append(us08.UserStory08())
    stories.append(us09.UserStory09())
    stories.append(us29.UserStory29())
    stories.append(us31.UserStory31())
    stories.append(us33.UserStory33())
    stories.append(us41.UserStory41())

    for story in stories:
        story.fire(conn)

if __name__ == '__main__':
    main()