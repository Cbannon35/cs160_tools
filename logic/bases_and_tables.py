'''

A file to store the id of the base and tables

'''
## BASES AND TABLES ##
BASE_ID = "appPa8qmBuak7pi4T"
ABSENCE_TABLE = "tbl9CqHmy6pVmdxYQ"

def get_table(flag: str) -> str:
    '''Returns the table name based on the flag'''
    if flag == 'absence':
        return ABSENCE_TABLE
    elif flag == 'extension':
        raise NotImplementedError("Extension table not implemented yet")
    else:
        raise ValueError("Invalid flag passed to get_table in bases_and_tables.py")

