[![Build Status](https://travis-ci.com/Agile555/GEDCOMProj.svg?branch=master)](https://travis-ci.com/Agile555/GEDCOMProj)

# :tada::tada::tada: Welcome to GEDCOM Dragonfruit :dragon: :tada::tada::tada: 

## New Things In Version 1.0.3:

This sprint, we implemented another __2__ user stories, putting us up to a total of 32!  You may be wondering why our user story output for this round is so low.  That is because this was actually a _hardening sprint_ for us -- yay for better code!

New features include:

* Handling of invalid dates
* Fresh, never frozen codebase

Sad news: this is actually the end of our GEDCOM journey. :cry: We all had a great time working together and hope to do something similar again.  As always, if you like our code, feel free to reach out to us at our GitHub handles! We're always working on something new :nerd_face:

# Get Ready for the Experience of a Lifetime

Welcome to the greatest, most _agile_ git repository of all time.  It is our job to take on megatron (the database we'll be working with) while fending off hordes of user stories fed by a mad product owner.  Will the developer team be able to escape within deadlines? Stick around and find out.

## Rules of the Craft
Please make sure that you `git fetch` and `git pull` before you start work on something, just to be sure you have the most recent version.  Also be sure to modularize your code, following the current design structure whenever possible.

## Style Guide

### Function Naming
Function names should be descriptive and use `snake_case`.  These don't need to be Java length names, but a couple of words goes a long way.

### Function Documentation
All functions must have a supporting document string following the Google Python Style Guide ([see](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)).  The description of the function should include the general operation as well as any complex logic.  For example:

```python
def sum_two_numbers(num1, num2):
    """
    This complex mathematical operation is yielded by the laws of addition.  Please reference Goldstein and Harowitz 
    for more information, chapters 15-17.  The first numbers value is added to the value of the second number and the resulting mathematical expression is returned.

    Args:
        num1 (int): the first number in the addition operation
        num2 (int): the second number in the addition operation

    Returns:
        (int): the result of the addition operation
    """
    return num1 + num2
```

### Modules
If starting a new module, please specify a docstring at the top specifying the user story that this module helps satisfy as well as the author(s).  Python has no built-in support for encapsulation in modules, however, all private methods of a module should be prefixed with an underscore.  For example:

```python
"""
Module providing absolute value functions.

@author:  Mark Freeman
"""

def _is_negative(num):
    """
    Determines if a number is negative or not.

    Args:
        num (int): the number in question

    Returns:
        (bool): the number is negative
    """
    if(num < 0):
        return True
    return False

def absolute_value(num):
    """
    Gives the absolute value of a number.

    Args:
        num (int): the number to take absolute value of

    Returns:
        (int): the absolute value of the number in question
    """
    if(_is_negative(num)):
        return num * -1
    return num
```
## On Skeletons, Tests, and User Stories
The current project skeleton follows this general format:

```bash
root
├── ged
│   ├── a.ged
│   ├── bunch.ged
│   ├── of.ged
│   ├── ged.ged
│   └── files.ged
├── tests
│   └── test_01_that_calls_ged_files.py
├── modules
│   └── user_story_01.py
├── lib
│   └── parser.py
│   └── tags.py
│   └── user_story.py
│   └── utilities.py
├── index.py
├── megatron.db
└── requirements.txt
```

All testing will be done via `pytest`.  Hence, all testing functions should be stored as a `test_something` file under the `tests` directory.  If the testing functions are not placed here, Travis will not see them.  To run the test suite, simply run `pytest tests` from the project root.

Similarly, all .ged files which support tests should be placed in the `ged` directory.  When testing, be sure to import the `execute_test` function after importing it from `lib.utilities.py`.  This simplifies testing, as you will not need to worry about database schemas or clearing out previous test results.  When supplying the name of your test to this function, simply specify the name of the file within the `ged` directory, do not provide a path.

### Writing Tests
Test cases do not need to adhere to the same style guide as all other modules.  Tests should still have a preamble docstring naming which user story the file is for, as well as the author name(s), but docstrings inside of functions are not necessary.  Instead, simply define what you are passing to the test and checking.  For example:

```python
"""
Test to find goats in the tree, User Story 01

@author: Mark Freeman
"""

from modules.us01 import UserStory01
from lib.utilities import execute_test
from sqlite3 import connect

conn = connect(':memory:')
user_story_01 = UserStory01()

#one goat placed in the tree that can be removed
def test_us01_01():
    execute_test('us01_01.ged', conn)
    assert get_rows(conn) == []

#multiple goats that simply refuse to leave the tree
def test_us01_02():
    execute_test('us01_02.ged', conn)
    assert get_rows(conn) == [('This is a row of interest to this test'), ('Another import condition')]
    
#...and so on
```

### Writing User Stories
User stories all share some basic functionalities: they should be able to query a database for rows of interest to them and print messages to the user that detail information from those rows.  Hence, all user stories will extend from the abstract class `UserStory` implemented in _lib/user_story.py_. To instantiate this class, developers will need to implement two basic methods -- `get_rows` and `print_rows`.  For example:

```python
"""
User Story 02 alerts the user to any dogs who are found to be good boys

@author Mark Freeman
"""

from lib.user_story import UserStory

class UserStory02(UserStory):

    def print_rows(rows):
        for row in rows:
            print('{} is a good boy!'.format(row[0]))
            #we assume list has [(name, is_good_boy), ...]
            
    def get_rows(conn)
        c = conn.cursor()
        rows = c.execute('SELECT name FROM dogs WHERE is_good_boy = 1').fetchall()
        #sometimes rows must be filtered further, see modules folder
        return rows
```
Some user stories may need to flesh out this pattern slightly more.  For example, to support a date range functionality, `datetime` may need to be imported.  Construction of a more complete return variable or further SQL queries may also be necessary.

## Feature Promotion

As you develop and complete user stories, please do not commit to `master`. That would be bad.  Instead, open up a new branch from `dev` each time you intend to create a new feature.  This helps to keep things encapsulated.

Once you have tested your new user story locally and assured proper functionality, you may then merge your branch up to `dev`.  Then, just as before, open a new branch if you want to start a new feature.  Every so often, we will then take all of the completed user stories and merge them up to `master`.

### Example

```bash
# I'm now going to start a feature, can also branch via github.com
git checkout -b name_of_my_feature dev

# ... going along doing some work
git add super_cool_python_file.py
git commit -m "Start user story 44"

# ... and all done
git add super_cool_python_file.py
git commit -m "Finish user story 44"

# First merge the branch into dev
git checkout dev
git merge name_of_my_feature

# Delete the old branch
git branch -d name_of_my_feature

# ... 

# Now I want to start a new user story
git checkout -b another_feature_name dev

# ... and so on

```

### Pull Requests

To merge a branch, you will need to open a pull request stating a general summary of the change.  This will very often just be what user story you are completing.  Pull requests to `dev` will require approval by at least 2 developers.  Pull requests to `master` will need approval from 3.  You cannot approve your own pull request.

## Purpose of this Project

This project is being created in response to SSW555, a course on agile methodologies at Stevens taught by Professor Rowland.  Four students are teaming up to take on this project using tactics such as pair programming, scrum, and continuous integration.

We'll see you on the other side!
