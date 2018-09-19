#Mark Freeman, SSW555

from prettytable import from_db_cursor
import datetime
import sqlite3

conn = sqlite3.connect('megatron.db')
c = conn.cursor()

d = { #not all tags have parallels, but all headers come from one or more tags
    'INDI': {
        'level': '0',
        'parents': [],
        'backwards': True,
        'parallel': 'ID',
        'number_of_attributes': 9
    },
    'FAM': {
        'level': '0',
        'parents': [],
        'backwards': True,
        'parallel': 'ID',
        'number_of_attributes': 8
    },
    'HEAD': {
        'level': '0',
        'parents': [],
        'backwards': False
    },
    'TRLR': {
        'level': '0',
        'parents': [],
        'backwards': False
    },
    'NOTE': {
        'level': '0',
        'parents': [],
        'backwards': False
    },
    'NAME': {
        ''
        'level': '1',
        'parents': ['INDI'],
        'backwards': False,
        'parallel': 'Name'
    },
    'SEX': {
        'level': '1',
        'parents': ['INDI'],
        'backwards': False,
        'parallel': 'Gender'
    },
    'BIRT': {
        'level': '1',
        'parents': ['INDI'],
        'backwards': False,
        'parallel': 'Birthday'
    },
    'DEAT': {
        'level': '1',
        'parents': ['INDI'],
        'backwards': False,
        'parallel': 'Death'
    },
    'FAMC': {
        'level': '1',
        'parents': ['INDI'],
        'backwards': False,
        'parallel': 'Child'
    },
    'FAMS': {
        'level': '1',
        'parents': ['INDI'],
        'backwards': False,
        'parallel': 'Spouse'
    },
    'MARR': {
        'level': '1',
        'parents': ['FAM'],
        'backwards': False,
        'parallel': 'Married'
    },
    'HUSB': {
        'level': '1',
        'parents': ['FAM'],
        'backwards': False,
        'parallel': 'Husband ID'
    },
    'WIFE': {
        'level': '1',
        'parents': ['FAM'],
        'backwards': False,
        'parallel': 'Wife ID'
    },
    'DIV': {
        'level': '1',
        'parents': ['FAM'],
        'backwards': False,
        'parallel': 'Divorced'
    },
    'CHIL': {
        'level': '1',
        'parents': ['FAM'],
        'backwards': False,
        'parallel': 'Children'
    },
    'DATE': {
        'level': '2',
        'parents': ['BIRT', 'DEAT', 'DIV', 'MARR'],
        'backwards': False
    }
}

#inflate a dictionary to hold the tags and their position in the table
indiTableTags = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
famTableTags = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
i = {
    'INDI': dict(zip(indiTableTags, range(len(indiTableTags)))),
    'FAM': dict(zip(famTableTags, range(len(famTableTags))))
}

stack = [] #controls parent-child relationships among tags
cursor = [] #modifiable buffer to hold data to be inserted into DB

#################### Stack Methods #####################

def isProperChild(tagName):
    for tag in stack: #search the stack for the parent to deem if it can go on
        if(tag in d.get(tagName).get('parents')):
            return True
    return False

def repairStack(tagName):
    global stack #forgive me
    if(d.get(tagName).get('level') == '0'): #if it's level 0, empty the stack and replace bottom with new tag
        stack = [tagName]
    elif(d.get(tagName).get('level') == '1'): #if it's level 1, replace second to last element and remove all others
        stack = [stack[0], tagName]

def adjustEntries(type): #after filling in direct related tags, fill secondary related
    if(type == 'INDI'):
        if(exists(cursor[i[type]['Birthday']])): #we were given a birth date, must fill in age
            if(exists(cursor[i[type]['Death']])): #age will diff between age and death
                append(i[type]['Age'], (cursor[i[type]['Death']] - cursor[i[type]['Birthday']]).days // 365) #TODO: technically not right with leap years
            else: #didn't die, age is diff between birth and now
                append(i[type]['Age'], (datetime.date.today() - cursor[i[type]['Birthday']]).days // 365)
        if(exists(cursor[i[type]['Death']])):
            append(i[type]['Alive'], 'N')
        else:
            append(i[type]['Alive'], 'Y')
    elif(type == 'FAM'):
        addSpouseNames(cursor[i[type]['Husband ID']], cursor[i[type]['Wife ID']])

#################### Database Methods ##################

def searchDB(table, column, name, value):
    return c.execute("SELECT {} FROM {} WHERE {}='{}'".format(column, table, name, value)) #for some reason SQLite wants them in quotes

def insertIntoDB(table, lst):
    if(table == 'INDI'):
        return c.execute('INSERT INTO INDI VALUES (?,?,?,?,?,?,?,?,?)', lst)
    if(table == 'FAM'):
        return c.execute('INSERT INTO FAM VALUES (?,?,?,?,?,?,?,?)', lst)

#################### Cursor Methods ####################

def emptyCursor(num_slots): #sometimes global is a necessary evil
    global cursor
    cursor = ["NA"] * num_slots

def append(index, str):
    global cursor
    if(exists(cursor[index])):
        cursor[index] = ",".join([cursor[index], str])
    else:
        cursor[index] = str

def addSpouseNames(husb, wife):
    val = searchDB('INDI', 'Name', 'ID', husb).fetchone()
    if(val):
        append(i['FAM']['Husband Name'], val[0]) #it's a cursor, need to subscript
    val = searchDB('INDI', 'Name', 'ID', wife).fetchone()
    if(val):
        append(i['FAM']['Wife Name'], val[0])

def exists(str):
    return (str != 'NA')

#################### Tag Methods #######################

def isBackWardTag(str):
    if(d.get(str) and d.get(str).get('backwards')):
        return True
    return False
    
def isValidLevel(tagName, level):
    if(d.get(tagName) and d.get(tagName).get('level') == level):
        return True
    return False

#################### Main Methods ######################

def createMessage(tagName, level, letter, args):
    return '<--' + level + '|' + tagName + '|' + letter + '|' + " ".join(args)

def process(line): #goal is to make sure that it is at its own valid level AND preceding a parent
    arr = line.split(" ")
    level, tagName, args = arr[0], None, [] #we know the level always

    #phase 1: assign variables
    if(len(arr) == 2):
        tagName = arr[1]
    elif(len(arr) > 2): #we know we have three, now check if it's backwards
        if(isBackWardTag(arr[1])): #if there's a backward tag in the wrong spot, don't bother
            tagName, args = arr[1], arr[2:]
            return createMessage(tagName, level, 'N', args)
        if(isBackWardTag(arr[2])):
            tagName, args = arr[2], [arr[1]]
        else:
            tagName, args = arr[1], arr[2:]

    #phase 2: add rows based on what was assigned, soon won't need to print lines
    if(isValidLevel(tagName, level)): #we have the tagName and level, assure that they are compatible
        if(level == '0'):
            if(isBackWardTag(tagName)): #only backward tags constitute a new entry
                if(cursor): #if one is already populated, go and insert it
                    adjustEntries(stack[0])
                    insertIntoDB(stack[0], cursor)
                repairStack(tagName)
                emptyCursor(d[tagName]['number_of_attributes']) #empty
                append(i[tagName][d[tagName]['parallel']], " ".join(args)) #insert id
                #now we have a cursor with the id filled that we can use
            return createMessage(tagName, level, 'Y', args)
        elif(level == '1'):
            if(isProperChild(tagName)):
                repairStack(tagName)
                if(args): #we don't want to overwrite the NA if we have no args to put there anyways
                    append(i[stack[0]][d[tagName]['parallel']], " ".join(args))
                return createMessage(tagName, level, 'Y', args)
            else:
                return createMessage(tagName, level, 'N', args)
        else: #level is 2, so far only date can have this so I'll throw a strip time right in and not check
            if(isProperChild(tagName)):
                repairStack(tagName)
                parent = stack[-1] #the last element on the stack is the immediate parent we need to modify with date
                append(i[stack[0]][d[parent]['parallel']], datetime.datetime.strptime(" ".join(args), '%d %b %Y').date())
                return createMessage(tagName, level, 'Y', args)
            else:
                return createMessage(tagName, level, 'N', args)
    else:
        return createMessage(tagName, level, 'N', args) #it wasn't a tag or it wasn't a valid level for that tag

def main():
    file_name = input('Please enter the name of the file you wish to validate: ')
    #file_name = 'tests/family.ged' or 'test/proj02test.ged' for debugging
    with open(file_name, 'r') as f:

        for line in f:
            line = line.strip('\n') #take off the newline
            print('-->' + line)
            print(process(line))

        adjustEntries(stack[0])
        insertIntoDB(stack[0], cursor)

        #go grab the sql tables
        print(from_db_cursor(c.execute('SELECT * FROM INDI ORDER BY ID ASC')))
        print(from_db_cursor(c.execute('SELECT * FROM FAM  ORDER BY ID ASC')))
        conn.commit() #save db every time it's run

if __name__ == '__main__':
    main()