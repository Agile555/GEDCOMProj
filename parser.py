#Mark Freeman, SSW555

from prettytable import PrettyTable

d = {
    'INDI': {
        'level': '0',
        'parents': [],
        'takesArgs': True,
        'backwards': True,
        'parallel': {
            'name': 'ID',
            'index': 0
        },
        'number_of_attributes': 9,
        'table': PrettyTable()
    },
    'FAM': {
        'level': '0',
        'parents': [],
        'takesArgs': True,
        'backwards': True,
        'parallel': {
            'name': 'ID',
            'index': 0
        },
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
        'parallel': {
            'name': 'Name',
            'index': 1
        }
    },
    'SEX': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False,
        'parallel': {
            'name': 'Gender',
            'index': 2
        }
    },
    'BIRT': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': False,
        'backwards': False,
        'parallel': {
            'name': 'Birthday',
            'index': 3
        }
    },
    'DEAT': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': False,
        'backwards': False,
        'parallel': {
            'name': 'Death',
            'index': 6
        }
    },
    'FAMC': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False,
        'parallel': {
            'name': 'Child',
            'index': 7
        }
    },
    'FAMS': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False,
        'parallel': {
            'name': 'Spouse',
            'index': 8
        }
    },
    'MARR': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': False,
        'backwards': False,
        'parallel': {
            'name': 'Married',
            'index': 1
        }
    },
    'HUSB': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False,
        'parallel': {
            'name': 'Husband ID',
            'index': 3
        }
    },
    'WIFE': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False,
        'parallel': {
            'name': 'Wife ID',
            'index': 5
        }
    },
    'DIV': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': False,
        'backwards': False,
        'parallel': {
            'name': 'Divorced',
            'index': 2
        }
    },
    'CHIL': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False,
        'parallel': {
            'name': 'Children',
            'index': 7
        }
    },
    'DATE': {
        'level': '2',
        'parents': ['BIRT', 'DEAT', 'DIV', 'MARR'],
        'takesArgs': True,
        'backwards': False
    }
}

#could use enum as well, but let's just dictionary these for now
#TODO: merge this into the main dictionary, pretty sure it can be done
#2 things with it:
#1) How do I get the field naems generated?
#2) How do I append into the cursor using it?
           
indices = {
    'INDI': ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'],
    'FAM': ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
}

stack = []
cursor = []
d['INDI']['table'].field_names = indices['INDI']
d['FAM']['table'].field_names = indices['FAM']

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
#TODO: see about removing many of these create message calls, maybe try except and place no in the except?
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
                if(cursor): #if one is already populated, go and insert it
                    d[stack[0]]['table'].add_row(cursor) #must be before repairing the stack
                repairStack(tagName)
                cursor = ["NA"] * d.get(tagName)['number_of_attributes'] #fancy
                cursor[d[stack[0]]['parallel']['index']] = " ".join(args) #insert id
                #now we have a cursor with the id filled that we can use
            return createMessage(tagName, level, 'Y', args)
        #TODO: think about consolidating these two blocks as they both make similar calls
        elif(level == '1'):
            if(isProperChild(tagName)):
                repairStack(tagName)
                cursor[d[tagName]['parallel']['index']] = " ".join(args)
                return createMessage(tagName, level, 'Y', args)
            else:
                return createMessage(tagName, level, 'N', args)
        else: #level is 2
            if(isProperChild(tagName)):
                repairStack(tagName)
                parent = stack[-1] #the last element on the stack is the immediate parent we need to modify
                cursor[d[parent]['parallel']['index']] = " ".join(args)
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

        d[stack[0]]['table'].add_row(cursor) #clear out the residual item on the stack

        print(d['INDI']['table'])
        print(d['FAM']['table'])

if __name__ == '__main__':
    main()