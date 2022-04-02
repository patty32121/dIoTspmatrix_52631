from position import *


spmatrix = [float, dict[position, float]]

def spmatrix_create(zero: float = 0) -> spmatrix:
    """
    Creatspmatrix
    e a new sparse matrix with zero parameter as zero/null – the default zero of a sparse matrix is 0
    If arguments are invalid => raise exception ValueError with message “spmatrix_create: invalid arguments”
    """
    if not (isinstance(zero, float) or isinstance(zero, int) ) or not ( zero >= 0 ):
        raise ValueError('spmatrix_create: invalid arguments')
    if (isinstance(zero, int)):
        zero = float(zero)
    my_dict = {}
    if zero == "":
        my_matrix = [0, my_dict]
    else:
        my_matrix = [zero, my_dict]
    return my_matrix

def spmatrix_is(mat: spmatrix) -> bool:
    """
    Validate if the input parameter mat is a valid sparse matrix, returning True if yes and False if otherwise
    """  
    if not (isinstance(mat, list) and (isinstance(mat[0], float) or isinstance(mat[0], int))):
        return False
    else :
        return True

def spmatrix_zero_get(mat: spmatrix) -> float:
    """
    Get the zero/null of the sparse matrix mat passed as input parameter
    If arguments are invalid => raise exception ValueError with message “spmatrix_zero_get: invalid arguments”
    """
    if not (isinstance(mat, list) and (isinstance(mat[0], float) or isinstance(mat[0], int))):
        raise ValueError('spmatrix_zero_get: invalid arguments')
    else: 
        return mat[0]

def spmatrix_zero_set(mat: spmatrix, zero: float):
    """
    Change the zero/null element of the sparse matrix mat to zero value passed as input parameter
    All the existing elements in the sparse matrix mat which are equal to the new zero/null are to be removed
    If arguments are invalid => raise exception ValueError with message “spmatrix_zero_set: invalid arguments”
    """
    if not (isinstance(mat, list) and (isinstance(mat[0], float) or isinstance(mat[0], int)) and mat[0] >= 0) or not (isinstance(zero,float)):
        raise ValueError('spmatrix_zero_set: invalid arguments')
    else: 
        mat[0] = zero
        return mat[0]

def spmatrix_value_get(mat: spmatrix, pos: position) -> float:
    """Retrieve the value from the sparse matrix mat from the given position pos passed as input parameter
    If arguments are invalid => raise exception ValueError with message “spmatrix_value_get: invalid arguments”
    """
    my_dict = mat[1]
    if not ((isinstance(mat, list) and (isinstance(mat[0], float) or isinstance(mat[0], int)) and mat[0] >= 0) or not (isinstance(pos, tuple) and len(pos == 2) and isinstance(pos[0], int) and isinstance(pos[1], int) and pos[0] >=0 and pos[1] >=0)):
        raise ValueError('spmatrix_zero_get: invalid arguments')
    else:
        value = my_dict.get(pos) 
        return value

def spmatrix_value_set(mat: spmatrix, pos: position, val: float):
    """Set a new value to the sparse matrix mat from at given position pos with value val passed as input parameters
    If arguments are invalid => raise exception ValueError with message “spmatrix_value_set: invalid arguments”
    """
    my_dict = mat[1]
    if not ((isinstance(mat, list) and (isinstance(mat[0], float) or isinstance(mat[0], int)) and mat[0] >= 0) or not (isinstance(pos, tuple) and len(pos == 2) and isinstance(pos[0], int) and isinstance(pos[1], int) and pos[0] >=0 and pos[1] >=0)):
        raise ValueError('spmatrix_zero_set: invalid arguments')
    if not (isinstance(val,float)):
        val = float(val)
        my_dict[pos] = val
    else:
        my_dict = mat[1]
        my_dict[pos] = val

def spmatrix_copy(mat: spmatrix) -> spmatrix:
    """
    Create a copy of the sparse matrix mat passed as input parameter
    If arguments are invalid => raise exception ValueError with message “spmatrix_copy: invalid arguments”
    """
    spmatrix2 = mat.copy()
    zero = spmatrix2[0]
    my_dict = spmatrix2[1]
    if not ((isinstance(mat, list) and (isinstance(zero, float) or isinstance(zero, int)) and zero >= 0)):
        raise ValueError('spmatrix_copy: invalid arguments')
    else: 
        spmatrix2 = mat
        return spmatrix2

def spmatrix_dim(mat: spmatrix) -> tuple[position, position]:
    """
    Get the dimension of the sparse matrix mat passed as input parameter as a tuple with a pair of positions containing the minimum and maximum coordinates of the sparse matrix elements, or an empty tuple if the sparse matrixcontains no elements
    If arguments are invalid => raise exception ValueError with message “spmatrix_dim: invalid arguments”
    """

def spmatrix_sparsity(mat: spmatrix) -> float:
    """
    Get the sparsity (density) of sparse matrix mat as the number of elements divided by the total number of elements (dimension)
    If arguments are invalid => raise exception ValueError with message “spmatrix_sparsity: invalid arguments”
    """

def spmatrix_str(mat: spmatrix, format: str) -> str:
    """
    Get the representation of the sparse matrix mat as a text string, one line of text per matrix line and for the overall matrix dimension
    The values of the elements of the sparse matrix are represented with the formatting defined in the format input parameter (e.g., ‘%.1f’)
    If arguments are invalid => raise exception ValueError with message ‘spmatrix_str: invalid arguments’
    """

def spmatrix_row(mat: spmatrix, row: int) -> spmatrix:
    """
    Retrieve the row (row number passed as parameter) of the sparse matrix mat as a new sparse matrix
    If arguments are invalid => raise exception ValueError with message ‘spmatrix_row: invalid arguments’
    """

def spmatrix_col(mat: spmatrix, col: int) -> spmatrix:
    """
    Retrieve the column (column number passed as parameter) of the sparse matrix mat as a new sparse matrix
    If arguments are invalid => raise exception ValueError with message ‘spmatrix_column: invalid arguments’
    """

    """def spmatrix_diagonal(mat: spmatrix) -> [spmatrix, ...]:"""
    """
    Retrieve the diagonal of the sparse matrix mat as a new sparse matrix considering the sparse matrix dimension   
    If arguments are invalid => raise exception ValueError with message ‘spmatrix_diagonal: invalid arguments’
    If sparse matrix mat is not square => raise exception ValueError with message ’spmatrix_diagonal: matrix not square’
    """
