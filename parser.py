#Mark Freeman, SSW555

from prettytable import PrettyTable

d = {
    'INDI': {
        'level': '0',
        'parents': [],
        'takesArgs': True,
        'backwards': True,
        'parallel': 'ID',
        'number_of_attributes': 9,
        'table': PrettyTable()
    },
    'FAM': {
        'level': '0',
        'parents': [],
        'takesArgs': True,
        'backwards': True,
        'parallel': 'ID',
        'number_of_attributes': 8,
        'table': PrettyTable()
    },
    'HEAD': {
        'level': '0',
        'parents': [],
        'takesArgs': False,
        'backwards': False
    },
    'TRLR': {
        'level': '0',
        'parents': [],
        'takesArgs': False,
        'backwards': False
    },
    'NOTE': {
        'level': '0',
        'parents': [],
        'takesArgs': True,
        'backwards': False
    },
    'NAME': {
        ''
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False,
        'parallel': 'Name'
    },
    'SEX': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False,
        'parallel': 'Gender'
    },
    'BIRT': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': False,
        'backwards': False,
        'parallel': 'Birthday'
    },
    'DEAT': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': False,
        'backwards': False,
        'parallel': 'Death'
    },
    'FAMC': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False,
        'parallel': 'Child'
    },
    'FAMS': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False,
        'parallel': 'Spouse'
    },
    'MARR': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': False,
        'backwards': False,
        'parallel': 'Married'
    },
    'HUSB': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False,
        'parallel': 'Husband ID'
    },
    'WIFE': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False,
        'parallel': 'Wife ID'
    },
    'DIV': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': False,
        'backwards': False,
        'parallel': 'Divorced'
    },
    'CHIL': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False,
        'parallel': 'Children'
    },
    'DATE': {
        'level': '2',
        'parents': ['BIRT', 'DEAT', 'DIV', 'MARR'],
        'takesArgs': True,
        'backwards': False
    }
}

#could use enum as well, but let's just dictionary these for now
indices = {
    'individuals': {
        'ID': 0,
        'Name': 1,
        'Gender': 2,
        'Birthday': 3,
        'Age': 4,
        'Alive': 5,
        'Death': 6,
        'Child': 7,
        'Spouse': 8
    },
    'families': {
        'ID': 0,
        'Married': 1,
        'Divorced': 2,
        'Husband ID': 3,
        'Husband Name': 4,
        'Wife ID': 5,
        'Wife Name': 6,
        'Children': 7
    }
}

stack = []
cursor = []
d['INDI']['table'].field_names = indices['individuals'].keys()
d['FAM']['table'].field_names = indices['individuals'].keys()

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

    #phase 2: add rows based on what was assigned
    if(isValidLevel(tagName, level)): #we have the tagName and level, assure that they are compatible
        if(level == '0'): #SOME level 0 tags indicate a new entry, not all
            if(isBackWardTag(tagName)): #only backward tags constitute a new entry
                repairStack(tagName)
                if(cursor): #if one is already populated, go and insert it
                    d[tagName]['table'].add_row(cursor)
                cursor = ["NA"] * d.get(tagName)['number_of_attributes'] #fancy
                #now we have a cursor that we should use
            return createMessage(tagName, level, 'Y', args)
        else:
            if(isProperChild(tagName)):
                repairStack(tagName)
                #TODO: append to the cursor we already have
                return createMessage(tagName, level, 'Y', args)
            else:
                return createMessage(tagName, level, 'N', args)
    else:
        return createMessage(tagName, level, 'N', args) #it wasn't a tag or it wasn't a valid level for that tag

def main():
    #file_name = input('Please enter the name of the file you wish to validate: ')
    file_name = 'tests/proj02test.ged'
    with open(file_name, 'r') as f:

        for line in f:
            line = line.strip('\n') #take off the newline
            print('-->' + line)
            print(process(line))

if __name__ == '__main__':
    main()