#Mark Freeman, SSW555

from prettytable import PrettyTable

d = {
    'INDI': {
        'level': '0',
        'parents': [],
        'takesArgs': True,
        'backwards': True
    },
    'FAM': {
        'level': '0',
        'parents': [],
        'takesArgs': True,
        'backwards': True
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
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False
    },
    'SEX': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False
    },
    'BIRT': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': False,
        'backwards': False
    },
    'DEAT': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': False,
        'backwards': False
    },
    'FAMC': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False
    },
    'FAMS': {
        'level': '1',
        'parents': ['INDI'],
        'takesArgs': True,
        'backwards': False
    },
    'MARR': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': False,
        'backwards': False
    },
    'HUSB': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False
    },
    'WIFE': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False
    },
    'DIV': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': False,
        'backwards': False
    },
    'CHIL': {
        'level': '1',
        'parents': ['FAM'],
        'takesArgs': True,
        'backwards': False
    },
    'DATE': {
        'level': '2',
        'parents': ['BIRT', 'DEAT', 'DIV', 'MARR'],
        'takesArgs': True,
        'backwards': False
    }
}

stack = []

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

#goal is to make sure that it is at its own valid level AND preceding a parent
def main():
    file_name = input('Please enter the name of the file you wish to validate: ')
    with open(file_name, 'r') as f:

        for line in f:
            line = line.strip('\n') #take off the newline
            print('-->' + line)
            arr = line.split(" ")

            level, tagName, args = arr[0], None, [] #we know the level always

            print(stack)

            #phase 1: assign variables
            if(len(arr) == 2):
                tagName = arr[1]
            elif(len(arr) > 2): #we know we have three, now check if it's backwards
                if(isBackWardTag(arr[2])):
                    tagName, args = arr[2], [arr[1]]
                else:
                    tagName, args = arr[1], arr[2:]

            #phase 2: print based on what got assigned
            if(isValidLevel(tagName, level)): #we have the tagName and level, assure that they are compatible
                if(level == '0'): #level 0 tags don't have parents to check
                    repairStack(tagName)
                    print(createMessage(tagName, level, 'Y', args))
                else:
                    if(isProperChild(tagName)):
                        repairStack(tagName)
                        print(createMessage(tagName, level, 'Y', args))
                    else:
                        print(createMessage(tagName, level, 'N', args))
            else:
                print(createMessage(tagName, level, 'N', args)) #it wasn't a tag or it wasn't a valid level for that tag

if __name__ == '__main__':
    main()