# Get Ready for the Experience of a Lifetime

Welcome to the greatest, most _agile_ git repository of all time.  It is our job to take on megatron (the database we'll be working with) while fending off hordes of user stories fed by a mad product owner.  Will the developer team be able to escape within deadlines? Stick around and find out.

## Rules of the Craft
Please make sure that you `git fetch` and `git pull` before you start work on something, just to be sure you have the most recent version.  Also be sure to modularize your code, using new files whenever possible.

## Style Guide

### Function Naming
Function names should be descriptive and use `snake_case`.  These don't need to be Java length names, but a couple of words goes a long way.

### Function Documentation
All functions must have a supporting document string defining what the function takes in as parameters, what it outputs, the type of the variable, and a general description of what it does / how it works if the logic is complex.  For example:

```python
"""
This complex mathematical operation is yielded by the laws of addition.  Please reference Goldstein and Harowitz 
for more information, chapters 15-17.  The first numbers value is added to the value of the second number and the resulting mathematical expression is returned.

@param    num1    int   the first number in the addition operation
@param    num2    int   the second number in the addition operation
@return           int   the result of the addition operation
"""
def sum_two_numbers(num1, num2):
    return num1 + num2
```

### Modules
Modules must be implemented in their own file and then imported into `index.py`.  Please provide unit tests inside of your module that you execute on your own before pushing to the repository.

If starting a new module, please specify a docstring at the top specifying the user story that this module helps satisfy as well as the author(s).  Python has no built-in support for encapsulation in modules, however, all private methods of a module should be prefixed with an underscore.  For example:

```python
"""
Module providing absolute value functions.
@author:  Mark Freeman
"""

"""
Determines if a number is negative or not.

@param    num   int   the number in question
@return         bool  boolean stating that the number is negative
"""
def _is_negative(num):
    if(num < 0):
        return True
    return False

"""
Gives the absolute value of a number.

@param    num   int   the number to take absolute value of
@return         int   the absolute value of the number in question
"""
def absolute_value(num):
    if(_is_negative(num)):
        return num * -1
    return num
```

## Feature Promotion

As you develop and complete user stories, please do not commit to `master`. That would be bad.  Instead, open up a new branch from `dev` each time you intend to create a new feature.  This helps to keep things encapsulated.

Once you have tested your new user story locally and assured proper functionality, you may then merge your branch up to `dev`.  Then, just as before, reopen a new branch if you want to start a new feature.  Every so often, we will then take all of the completed user stories and merge them up to `master`.

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

To merge a branch, you will need to open a pull request stating a general summary of the change.  This will very often just be what user story you are completing.  Pull requests to `dev` will require approval by at least 2 developers.  Pull requests to `master` will need approval from 3.  You cannot approve our own pull request.

## Purpose of this Project

This project is being created in response to SSW555, a course on agile methodologies at Stevens taught by Professor Rowland.  Four students are teaming up to take on this project using tactics such as pair programming, scrum, and continuous integration.

We'll see you on the other side!
