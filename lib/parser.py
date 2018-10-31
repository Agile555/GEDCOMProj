"""
Main parser module that populates an SQLite database from a .ged input file.  Please note that this
parser does not support level 2 tags apart from the DATE tag.

@author: Mark Freeman
"""

from prettytable import from_db_cursor
from lib.tags import d, i
import datetime

stack = [] #controls parent-child relationships among tags
cursor = [] #modifiable buffer to hold data to be inserted into DB

#################### Stack Methods #####################

def is_proper_child(tag_name):
    """
    Determines if a tag is allowed in the place it is trying to be placed.  All tags below
    level 0 must be a proper child of the tag above them.

    Args:
        tag_name (string): the name of the tag we are 
            trying to insert

    Returns:
        (bool): the tag can be inserted here    
    """
    for tag in stack: #search the stack for the parent to deem if it can go on
        if(tag in d.get(tag_name).get('parents')):
            return True
    return False

def repair_stack(tag_name):
    """
    Fixes the stack as we insert objects.  Level 0 items will clear the stack completely, 
    while all others will clear the stack down to their level.

    Args:
        tag_name (string): the name of the tag to place 
            on the stack

    Returns:
        None
    """
    global stack #forgive me for I have sinned
    if(d.get(tag_name).get('level') == '0'): #if it's level 0, empty the stack and replace bottom with new tag
        stack = [tag_name]
    elif(d.get(tag_name).get('level') == '1'): #if it's level 1, replace second to last element and remove all others
        stack = [stack[0], tag_name]

#################### Database Methods ##################

def search_db(table, column, name, value, c):
    """
    SQLite wrapper to expose a simple selection query as a function.

    Args:
        table (string): the name of the table to search
        column (string): the column to return values from
        name (string): name of the value to match on
        value (string): value to match with
        c (cursor): An SQLite cursor object connecting us
            to the database

    Returns:
        (cursor): cursor representing all rows that 
            matched the search  
    """
    return c.execute("SELECT {} FROM {} WHERE {}='{}'".format(column, table, name, value)) #for some reason SQLite wants them in quotes

def insert_into_db(table, lst, c):
    """
    SQLite wrapper to expose an insertion query as a function.

    Args:
        table (string): the name of the table to insert into
        lst (list): a list of values to insert into 
            the database
        c (cursor): An SQLite cursor object connecting us
            to the database

    Returns:
        None
    """
    if(table == 'INDI'):
        c.execute('INSERT INTO INDI VALUES (?,?,?,?,?,?,?,?,?)', lst) #value schemes are different for different tables
    if(table == 'FAM'):
        c.execute('INSERT INTO FAM VALUES (?,?,?,?,?,?,?,?)', lst)
    if(table == 'CHLD'):
        c.execute('INSERT INTO CHLD VALUES (?,?)', lst)

#################### Cursor Methods ####################

def adjust_entries(type, c): #after filling in direct related tags, fill secondary related
    """
    Adjusts the cursor we build to include secondary entries, which are generated from
    direct entires.

    Definitions:
        Direct Entry: An entry in the cursor or table 
            which does not come directly from a tag.  
            For example, the `Name` attribute is 
            direct because it is populated directly
            by the NAME tag.
        Secondary Entry: A tag which does not correlate 
            directly to an entry in the cursor or table.  
            For example, the `Age` attribute is secondary 
            because it results from some combination of the
            `Birthday` and `Death` entries, which in turn 
            come directly from the BIRT and DEAT tags.
            
    Args:
        type (string): Either `INDI` or `FAM`, which 
            denotes the cursor format that is currently 
            being used
        c (cursor): An SQLite cursor object connecting us
            to the database

    Returns:
        None
    """
    if(type == 'INDI'):
        if(exists(cursor[i[type]['Birthday']])): #we were given a birth date, must fill in age
            if(exists(cursor[i[type]['Death']])): #age will diff between age and death
                append(i[type]['Age'], str((cursor[i[type]['Death']] - cursor[i[type]['Birthday']]).days // 365)) #TODO: technically not right with leap years
            else: #didn't die, age is diff between birth and now
                append(i[type]['Age'], str((datetime.date.today() - cursor[i[type]['Birthday']]).days // 365))
        if(exists(cursor[i[type]['Death']])):
            append(i[type]['Alive'], 'N')
        else:
            append(i[type]['Alive'], 'Y')
    elif(type == 'FAM'): #TODO: Need to add a list of children into the cursor
        add_children_to_db(cursor[i[type]['ID']], c) #go grab the family id and populate the children in the database with it
        add_spouse_names(cursor[i[type]['Husband ID']], cursor[i[type]['Wife ID']], c)
        add_ages_to_children(c) #User Story 28

def empty_cursor(num_slots): #sometimes global is a necessary evil
    """
    Empties and repopulates the cursor with an appropriate number of slots.  Generally called after an insertion.

    Args:
        num_slots (int): the number of "NA" slots to
            inflate the cursor with

    Returns:
        None
    """
    global cursor
    cursor = ["NA"] * num_slots

def append(index, str):
    """
    Appends an item to the cursor.  If the item already exists in the cursor, it forms a comma separated string of
    the values and inserts that.

    Args:
        index (int): the index of the cursor we are targeting

    Returns:
        str (string): the value to place at that index
    """
    global cursor
    if(exists(cursor[index])):
        cursor[index] = ",".join([cursor[index], str])
    else:
        cursor[index] = str

def add_children_to_db(family_id, c):
    """
    Adds children specified in the 'Children' column of the FAM cursor to the database. The value
    in the cursor will be a comma separated list of children IDs, which will be split and appended
    one by one to the db.

    Args:
        family_id (string): the ID of the family that each of these children belong to
        c (cursor): An SQLite cursor object connecting us to the database

    Returns:
        None
    """
    children = cursor[i['FAM']['Children']].split(',') #keep in mind, user IDs cannot have commas
    for child in children:
        insert_into_db('CHLD', [family_id, child], c)

def add_spouse_names(husb, wife, c):
    """
    Retrieve the names of the husband and wife of a family using their IDs and append their name to the cursor.

    Args:
        husb (string): id of the husband
        wife (string): id of the wife

    Returns:
        None
    """
    val = search_db('INDI', 'Name', 'ID', husb, c).fetchone()
    if(val):
        append(i['FAM']['Husband Name'], val[0]) #it's a cursor, need to subscript
    val = search_db('INDI', 'Name', 'ID', wife, c).fetchone()
    if(val):
        append(i['FAM']['Wife Name'], val[0])

def add_ages_to_children(c):
    """
    For every child already in the cursor, append their age.  Then, sort by age.

    Args:
        c (cursor): cursor object connecting us to SQL database

    Returns:
        None
    """
    unknowns = []
    knowns = []

    child_css = cursor[i['FAM']['Children']] #TODO: rename cursor (conflict of name with SQL cursor c)
    if(exists(child_css)):
        for child in child_css.split(','):
            age = search_db('INDI', 'Age', 'ID', child, c).fetchone()
            if(age and exists(age)): #kid was in the database and age was not NA
                knowns.append((age[0], child)) #we're gonna sort the tuple on the first element
            else:
                unknowns.append(('NA', child))
    
    out = []
    for child in list(reversed(sorted(knowns))) + unknowns:
        out.append('{} ({})'.format(child[1], child[0]))

    cursor[i['FAM']['Children']] = ', '.join(out) #finally, overwrite with ages added
    
def exists(str):
    """
    Checks to see whether the value is populated in the cursor

    Args:
        str (string): the value in the cursor

    Returns:
        (bool): the value is populated already in the cursor
    """
    return (str != 'NA')

#################### Tag Methods #######################

def is_backward_tag(str):
    """
    Checks to see if a tag is one of the backwards tags in GEDCOM, namely INDI and FAM.

    Args:
        str (string): the name of the tag to chck

    Returns:
        (bool): the tag is a backwards tag
    """
    if(d.get(str) and d.get(str).get('backwards')):
        return True
    return False
    
def is_valid_level(tag_name, level):
    """
    Checks to see if the tag is allowed at that level.  For instance, a DATE can never be
    applied at level 0 or 1, only 2.  This does not involve the stack.

    Args:
        tag_name (string): the name of the tag to check
        level (string): the attempted level of the tag

    Returns:
        (bool): the tag can be used at that level    
    """
    if(d.get(tag_name) and d.get(tag_name).get('level') == level):
        return True
    return False

#################### Main Methods ######################

def process(line, c): #goal is to make sure that it is at its own valid level AND preceding a parent
    """
    Main function of the parser.  Take in a line from a file as text and inspect it to gather
    information as to what it is trying to do.  Check if that is allowed, and if it is, go ahead
    and toss it into the database.  If not, don't bother.

    Args:
        line (string): one line of the GEDCOM file

    Returns:
        None
    """
    arr = line.split(" ")
    level, tag_name, args = arr[0], None, [] #we know the level always

    #phase 1: assign variables
    if(len(arr) == 2):
        tag_name = arr[1]
    elif(len(arr) > 2): #we know we have three, now check if it's backwards
        if(is_backward_tag(arr[1])): #if there's a backward tag in the wrong spot, don't bother
            tag_name, args = arr[1], arr[2:]
        if(is_backward_tag(arr[2])):
            tag_name, args = arr[2], [arr[1]]
        else:
            tag_name, args = arr[1], arr[2:]

    #phase 2: add rows based on what was assigned, soon won't need to print lines
    if(is_valid_level(tag_name, level)): #we have the tag_name and level, assure that they are compatible
        if(level == '0'):
            if(is_backward_tag(tag_name)): #only backward tags constitute a new entry
                if(cursor): #if one is already populated, go and insert it
                    adjust_entries(stack[0], c)
                    insert_into_db(stack[0], cursor, c)
                repair_stack(tag_name)
                empty_cursor(d[tag_name]['number_of_attributes']) #empty
                append(i[tag_name][d[tag_name]['parallel']], " ".join(args)) #insert id
                #now we have a cursor with the id filled that we can use
        elif(level == '1'):
            if(is_proper_child(tag_name)):
                repair_stack(tag_name)
                if(args): #we don't want to overwrite the NA if we have no args to put there anyways
                    append(i[stack[0]][d[tag_name]['parallel']], " ".join(args))
        else: #level is 2, so far only date can have this so I'll throw a strip time right in and not check
            if(is_proper_child(tag_name)):
                repair_stack(tag_name)
                parent = stack[-1] #the last element on the stack is the immediate parent we need to modify with date
                if(len(args) == 2): #they only gave us month and year
                    args = ['1'] + args
                if(len(args) == 1): #they only gave us a year
                    args = ['1', 'JAN'] + args 
                append(i[stack[0]][d[parent]['parallel']], datetime.datetime.strptime(" ".join(args), '%d %b %Y').date())

def parse(file, conn): #formerly main
    """
    Read in the GEDCOM file entered by the user and process each of them.  After the database
    is populated, show the contents of the tables.

    Args:
        file (string): a path to the file which we are planning to parse and store
        conn (connection): an SQLite connection object which represents the database
            we plan on writing information to

    Returns:
        None
    """
    global cursor
    cursor = [] #CRITICALLY IMPORTANT
    #TODO: Investigate and understand what the removal of these two lines does to the program.  The cursor
    #appears to stay behind after the parser function has completed and pollutes the next call to parser,
    #will erratically ruin test cases

    #TODO: Remove global variables, make everything local

    c = conn.cursor()
    with open(file, 'r') as f:

        for line in f:
            line = line.strip('\n') #take off the newline
            process(line, c)

    adjust_entries(stack[0], c)
    insert_into_db(stack[0], cursor, c)

    #go grab the sql tables
    print('\nIndividuals:')
    print(from_db_cursor(c.execute('SELECT * FROM INDI ORDER BY ID ASC')))
    print('\nFamilies:')
    print(from_db_cursor(c.execute('SELECT * FROM FAM  ORDER BY ID ASC')))
    conn.commit() #save db every time it's run