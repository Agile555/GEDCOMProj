# Get Ready for the Experience of a Lifetime

Welcome to the greatest, most _agile_ git repository of all time.  It is our job to take on megatron (the database we'll be working with) while fending off hordes of user stories fed by a mad product owner.  Will the developer team be able to escape within deadlines? Stick around and find out.

## Rules of the Craft
Please make sure that you `git fetch` and `git pull` before you start work on something, just to be sure you have the most recent version.  Also be sure to modularize your code, using new files whenever possible.

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
The project skeleton follows this general format:

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
├── index.py
├── parser.py
├── tags.py
├── utilities.py
├── megatron.db
└── requirements.txt
```

All testing will be done via `pytest`.  Hence, all testing functinos should be stored as a `test_something` file under the `tests` directory.  If the testing functions are not placed here, Travis will not see them.  To run the test suite, simply run `pytest tests` from the project root.

Similarly, all .ged files which support tests should be placed in the `ged` directory.  When testing, be sure to import the `execute_test` function after importing it from `utilities.py`.  This simplifies testing, as you will not need to worry about database schemas or clearing out previous test results.  When supplying the name of your test to this function, simply specify the name of the file within the `ged` directory, do not provide a path.

### Writing Tests
Test cases do not need to adhere to the same style guide as all other modules.  Tests should still have a preamble docstring naming which user story the file is for, as well as the author name(s), but docstrings inside of functions are not necessary.  For example:

```python
"""
Test to make sure no goats are in the tree, user story 42
@author: Mark Freeman
"""

from modules.my_user_story import get_rows
from utilities import execute_test
import sqlite3

conn = sqlite3.connect(':memory:')

def test_my_user_story_01():
    execute_test('my_user_story_01.ged', conn)
    assert get_rows(conn) == [] #checking all-good input

def test_my_user_story_02():
    execute_test('my_user_story_02.ged', conn)
    assert get_rows(conn) == [('This is a row of interest to this test'), ('Another import condition')] #checking bad input
    
#...and so on
```

### Writing User Stories
User stories all share some basic functionalities: they should be able to query a database for rows of interest to them and print messages to the user that detail information from those rows.  Hence, all user stories should support two basic methods -- `get_rows` and `_print_rows`.  For example:

```python
def _print_rows(rows): #private
    for row in rows:
        print('{} is a good boy!'.format(row[0])) #we assume list has [name, is_good_boy]
        
def get_rows(conn)
    c = conn.cursor()
    rows = c.execute('select name from dogs where is_good_boy = 1').fetchall() #sometimes rows must be filtered further
    return rows
    
def user_story(conn): #used by index.py to generate error messages when parsing user input files
    rows = get_rows(conn)
    print_rows(rows)
```
Some user stories may need to flesh out this pattern slightly more, but this can provide the basis for many user stories to build upon.

## Feature Promotion

As you develop and complete user stories, please do not commit to `master`. That would be bad.  Instead, open up a new branch from `dev` each time you intend to create a new feature.  This helps to keep things encapsulated.

Once you have tested your new user story locally and assured proper functionality, you may then merge your branch up to `dev`.  Then, just as before, open a new branch if you want to start a new feature.  Every so often, we will then take all of the completed user stories and merge them up to `master`.

Never commit directly to `dev` or to `master`.  This increases the odds of encountering a merge conflict.

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
