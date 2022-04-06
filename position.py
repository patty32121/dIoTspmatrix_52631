position = tuple[int, int]

def position_create(row: int, col: int) -> position:
    """
    Create a position based on the row and a column set as input parameters
    If arguments are invalid => raise exception ValueError with message ‘position_create: invalid arguments’
    """
    if not (type(row) is int and row >= 0) or not (type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col


def position_is(pos: position) -> bool:
    """
    Validate if the input parameter pos is a valid position, returning True if yes and False if otherwise
    """
    """if type(pos[0]) is int:
        pos[0] = (float)(pos[0])
    else: 
        return False
    if type(pos[1]) is int: 
        pos[1] = (float)(pos[1]) 
    else: 
        return False"""
    if not ((type(pos) is tuple) and (pos[0]>=0 and pos[1]>=0) and (len(pos)==2) and (type(pos[0]) is int) and (type(pos[1]) is int)):
        return False
        """isinstance(pos,int)"""
    else:
        return True
        

def position_row(pos: position) -> int:
    """
    Retrieve the row associated with the position pos passed as parameter to the function
    If arguments are invalid => raise exception ValueError with message ‘position_row: invalid arguments’
    """
    if not ((type(pos) is tuple and  pos[0] >= 0) or not (pos[0] is int)or not (len(pos)==2)):
        raise ValueError('position_row: invalid arguments')
    else:
        return pos[0]

def position_col(pos: position) -> int:
    """
    Retrieve the column associated with the position pos passed as parameter to the function
    If arguments are invalid => raise exception ValueError with message ‘position_col: invalid arguments’
    """
    if not ((type(pos) is tuple and  pos[1] >= 0) or not (pos[1] is int) or not (len(pos)==2)):
        raise ValueError('position_col: invalid arguments')
    else:
        return pos[1]


def position_equal(pos1: position, pos2: position) -> bool:
    """
    Compare if the two positions (pos1 and pos2) are equal, returning True if yes and False if otherwise
    If arguments are invalid => raise exception ValueError with message ‘position_equal: invalid arguments’
    """
    if not (type(pos1) is tuple and type(pos2) is tuple) :
        raise ValueError('position_equal: invalid arguments')
    if not (pos1[0] == pos2[0] and pos1[1] == pos2[1] and (len(pos1)==2) and (len(pos2)==2) and (type(pos1) is tuple) and (type(pos2) is tuple)):
        return False
    else:
        return True

def position_str(pos: position) -> str:
    """
    Get the representation of the position pos as a text string with the format ‘(row, column)’
    If arguments are invalid => raise exception ValueError with message ‘position_str: invalid arguments’"""
    if not ((type(pos) is tuple and  pos[1] >= 0 and pos[0]>=0) or not (pos[1] is int and pos[0] is int) or not (len(pos)==2)):
        raise ValueError('position_str: invalid arguments')
    pos1 = str(pos[0])
    pos2 = str(pos[1])
    pos_final = '(' + pos1 + ', ' + pos2 + ')'  
    return pos_final
