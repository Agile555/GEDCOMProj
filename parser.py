#Mark Freeman, SSW555

from prettytable import PrettyTable

#define globally our accepted tags
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

def empty(lst):
    while(lst != []):
        lst.pop()

def emptyToOne(lst):
    while(len(lst) < 1):
        lst.pop()

def isBackWardTag(str):
    if(d.get(str) and d.get(str).get('backwards')):
        return True
    return False

def isValidLevel(tagName, level):
    if(d.get(tagName) and d.get(tagName).get('level') == level):
        return True
    return False

#search the stack for the parent to deem if it can go on
def isProperChild(tagName):
    for tag in stack:
        if(tag in d.get(tagName).get('parents')):
            return True
    return False

#fix the stack after insertion, this only really occurs after a 1 or 2 insertion, as there is no level 3
#so state of level two does not need to be tracked
def repairStack(tagName):
    if(d.get(tagName).get('level') == '0'):
        empty(stack)
        stack.append(tagName)
    elif(d.get(tagName).get('level') == '1'):
        emptyToOne(stack) #would have had to pass a parent check, so stack cannot be 
        stack.append(tagName)

def printMessage(tagName, level, args, letter):
    print('<--' + level + '|' + tagName + '|' + letter + '|' + " ".join(args))

#goal is to make sure that it is at its own valid level AND preceding a parent
def main():
    file_name = input('Please enter the name of the file you wish to validate: ')
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip('\n') #take off the newline
            print('-->' + line)
            arr = line.split(" ")

            #we assume all lines, even invalid ones are forward tags until proven otherwise
            tagName = arr[1]
            level = arr[0]
            args = arr[2:]

            #there's a better way to do this, but block anyone sneaking in a backward tag in the first slot
            if(isBackWardTag(arr[1])):
                printMessage(tagName, level, args, 'N')
                continue

            if(len(arr) > 2):
                if(isBackWardTag(arr[2])): #if we were wrong, overwrite it
                    tagName = arr[2]
                    level = arr[0]
                    args = [arr[1]] #keep array so we can join later

            #now we have the tagName and level, assure that they are compatible
            if(isValidLevel(tagName, level)):
                #if we're going to 0, reset the stack with only that tag
                if(level == '0'):
                    repairStack(tagName)
                    printMessage(tagName, level, args, 'Y')
                else:
                    if(isProperChild(tagName)):
                        repairStack(tagName)
                        printMessage(tagName, level, args, 'Y')
                    else:
                        printMessage(tagName, level, args, 'N')
            else:
                #it wasn't a tag or it wasn't a valid level for that tag
                printMessage(tagName, level, args, 'N')

if __name__ == '__main__':
    main();