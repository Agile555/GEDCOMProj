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

stack = []
cursor = []

def adjustEntries(type): #after filling in direct related tags, fill secondary related
    global cursor #i am a truly lost man
    if(type == 'INDI'):
        if(exists(cursor[i[type]['Birthday']])): #we were given a birth date, must fill in age
            if(exists(cursor[i[type]['Death']])): #age will diff between age and death
                cursor[i[type]['Age']] = (cursor[i[type]['Death']] - cursor[i[type]['Birthday']]).days // 365 #TODO: technically not right with leap years
            else: #didn't die, age is diff between birth and now
                cursor[i[type]['Age']] = (datetime.date.today() - cursor[i[type]['Birthday']]).days // 365
        if(exists(cursor[i[type]['Death']])):
            cursor[i[type]['Alive']] = 'N'
        else:
            cursor[i[type]['Alive']] = 'Y'
    #TODO add query support
    elif(type == 'FAM'):
        addSpouseNames(cursor[i[type]['Husband ID']], cursor[i[type]['Wife ID']])

def append(index, str):
    global cursor
    if(exists(cursor[index])):
        cursor[index] = [cursor[index], str]
    else:
        cursor[index] = str

def exists(str):
    return (str != 'NA')

#TODO: name-ify
def addSpouseNames(husb, wife):
    global cursor
    val = searchDB('INDI', 'Name', 'ID', husb).fetchone()
    if(val):
        cursor[4] = val[0] #it's a cursor, need to subscript
    val = searchDB('INDI', 'Name', 'ID', wife).fetchone()
    if(val):
        cursor[6] = val[0]

def insertIntoDB(table, lst):
    if(table == 'INDI'):
        return c.execute('INSERT INTO INDI VALUES (?,?,?,?,?,?,?,?,?)', lst)
    if(table == 'FAM'):
        return c.execute('INSERT INTO FAM VALUES (?,?,?,?,?,?,?,?)', lst)
    
def searchDB(table, column, name, value):
    return c.execute("SELECT {} FROM {} WHERE {}='{}'".format(column, table, name, value)) #for some reason SQLite wants them in quotes

def isBackWardTag(str):
    if(d.get(str) and d.get(str).get('backwards')):
        return True
    return False

def isValidLevel(tagName, level):
    if(d.get(tagName) and d.get(tagName).get('level') == level):
        return True
    return False

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

def createMessage(tagName, level, letter, args):
    return '<--' + level + '|' + tagName + '|' + letter + '|' + " ".join(args)

#TODO: name-ify these cursor calls to make the code more idiomatic
def process(line): #goal is to make sure that it is at its own valid level AND preceding a parent
    arr = line.split(" ")
    level, tagName, args = arr[0], None, [] #we know the level always
    global cursor

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
                    print(cursor)
                    insertIntoDB(stack[0], cursor)
                repairStack(tagName)
                cursor = ["NA"] * d[tagName]['number_of_attributes'] #fancy
                
                cursor[i[tagName][d[tagName]['parallel']]] = " ".join(args) #insert id
                #now we have a cursor with the id filled that we can use
            return createMessage(tagName, level, 'Y', args)
        elif(level == '1'):
            if(isProperChild(tagName)):
                repairStack(tagName)
                cursor[i[stack[0]][d[tagName]['parallel']]] = " ".join(args)
                return createMessage(tagName, level, 'Y', args)
            else:
                return createMessage(tagName, level, 'N', args)
        else: #level is 2, so far only date can have this so I'll throw a strip time right in and not check
            if(isProperChild(tagName)):
                repairStack(tagName)
                parent = stack[-1] #the last element on the stack is the immediate parent we need to modify
                cursor[i[stack[0]][d[parent]['parallel']]] = datetime.datetime.strptime(" ".join(args), '%d %b %Y').date()
                return createMessage(tagName, level, 'Y', args)
            else:
                return createMessage(tagName, level, 'N', args)
    else:
        return createMessage(tagName, level, 'N', args) #it wasn't a tag or it wasn't a valid level for that tag

def main():
    #file_name = input('Please enter the name of the file you wish to validate: ')
    file_name = 'tests/family.ged'
    with open(file_name, 'r') as f:

        for line in f:
            line = line.strip('\n') #take off the newline
            print('-->' + line)
            print(process(line))

        adjustEntries(stack[0])
        insertIntoDB(stack[0], cursor)

        #go grab the sql tables
        print(from_db_cursor(c.execute('SELECT * FROM INDI')))
        print(from_db_cursor(c.execute('SELECT * FROM FAM')))
        conn.commit() #save db every time it's run

if __name__ == '__main__':
    main()