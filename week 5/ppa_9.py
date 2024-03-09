def get_column(mat, col):
    """
    extract a specific column from the matrix

    Arguments:
        mat: list of lists
        col: integer
    Return:
        col_list: list
    """
    col_list = []
    for i in mat:
        col_list.append(i[col])
    return col_list 

def get_row(mat, row):
    """
    extract a specific row from the matrix
    
    Arguments:
        mat: list of lists
        row: integer
    Return:
        row_list: list
    """
    return mat[row]
