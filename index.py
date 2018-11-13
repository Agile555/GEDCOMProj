"""
Entry point for GEDCOM parsing application.

@author: Mark Freeman, Michael Ameer, Besnik Balaj, Kipsy Quevada
"""

from modules import us01, us02, us03, us04, us05, us06, us07, us08, us09, us10, us12, us13, us15, us16, us18, us21, us23, us24, us27, us28, us29, us30, us31, us32, us33, us34, us35, us36, us38, us39, us41, us42
from lib.utilities import reset_db, execute_test
import sqlite3

def main():
    #set up the database
    conn = sqlite3.connect('megatron.db')
    reset_db(conn)

    #fill the database with our entire test suite as one file first
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
    stories.append(us10.UserStory10())
    stories.append(us12.UserStory12())
    stories.append(us13.UserStory13())
    stories.append(us15.UserStory15())
    stories.append(us16.UserStory16())
    stories.append(us18.UserStory18())
    stories.append(us21.UserStory21())
    stories.append(us23.UserStory23())
    stories.append(us24.UserStory24())
    stories.append(us27.UserStory27())
    stories.append(us28.UserStory28())
    stories.append(us29.UserStory29())
    stories.append(us30.UserStory30())
    stories.append(us31.UserStory31())
    stories.append(us32.UserStory32())
    stories.append(us33.UserStory33())
    stories.append(us34.UserStory34())
    stories.append(us35.UserStory35())
    stories.append(us36.UserStory36())
    stories.append(us38.UserStory38())
    stories.append(us39.UserStory39())
    stories.append(us41.UserStory41())
    stories.append(us42.UserStory42())

    for story in stories:
        story.fire(conn)

if __name__ == '__main__':
    main()
