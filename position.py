position = tuple[int, int]

def position_create(row: int, col: int) -> position:
    """
    Create a position
    :param row: row of position
    _param col: column of position
    :return: position
    """
    if not (type(row) is int and row >= 0) or not (type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col
