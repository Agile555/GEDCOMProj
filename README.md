# Get Ready for the Experience of a Lifetime

Welcome to the greatest, most _agile_ git repository of all time.  It is our job to take on megatron (the database we'll be working with) while fending off hordes of user stories fed by a mad product owner.  Will the developer team be able to escape within deadlines? Stick around and find out.

## Rules of the Craft
Please make sure that you `git fetch` and `git pull` before you start work on something, just to be sure you have the most recent version.  Also be sure to modularize your code, using new files whenever possible.

## Style Guide

### Function Naming
Function names should be descriptive and use `snake_case`.  These don't need to be Java length names, but a couple of words goes a long way.

### Function Commenting
All functions must have a supporting document string defining what the function takes in as parameters, what it outputs, the type of the variable, and a general description of what it does / how it works if the logic is complex.  For example:

```python
"""
This complex mathematical operation is yielded by the laws of addition.  Please reference Goldstein and Harowitz 
for more information, chapters 15-17.  The first numbers value is added to the value of the second number and the resulting mathematical expression is returned.

@param  num1  int  the first number in the addition operation
@param  num2  int  the second number in the addition operation
@return       int  the result of the addition operation
"""
def sum_two_numbers(num1, num2):
  return num1 + num2
```

### Modules
Modules must be implemented in their own file and then imported into `index.py`.  Please provide unit tests inside of your module that you execute on your own before pushing to the repository.

## Purpose of this Project

This project is being created in response to SSW555, a course on agile methodologies at Stevens taught by Professor Rowland.  Four students are teaming up to take on this project using tactics such as pair programming, scrum, and continuous integration.

We'll see you on the other side!
