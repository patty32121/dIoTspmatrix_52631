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
    if not (type(pos) is tuple[int,int] and pos[0]>=0):
        raise ValueError('position_create: invalid arguments')
    return pos
        

    



def position_row(pos: position) -> int:
    """
    Retrieve the row associated with the position pos passed as parameter to the function
    If arguments are invalid => raise exception ValueError with message ‘position_row: invalid arguments’
    """

def position_col(pos: position) -> int:
    """
    Retrieve the column associated with the position pos passed as parameter to the function
    If arguments are invalid => raise exception ValueError with message ‘position_col: invalid arguments’
    """

def position_equal(pos1: position, pos2: position) -> bool:
    """
    Compare if the two positions (pos1 and pos2) are equal, returning True if yes and False if otherwise
    If arguments are invalid => raise exception ValueError with message ‘position_equal: invalid arguments’
    """

def position_str(pos: position) -> str:
    """
    Get the representation of the position pos as a text string with the format ‘(row, column)’
    If arguments are invalid => raise exception ValueError with message ‘position_str: invalid arguments’"""

