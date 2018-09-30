"""
Collection of all of the GEDCOM tags which are supported.  Also defines relationships among the tags.

@author: Mark Freeman
"""

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
indi_table_tags = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
fam_table_tags = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
i = {
    'INDI': dict(zip(indi_table_tags, range(len(indi_table_tags)))),
    'FAM': dict(zip(fam_table_tags, range(len(fam_table_tags))))
}