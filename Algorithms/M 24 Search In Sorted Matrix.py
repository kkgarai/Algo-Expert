"""
Search In Sorted Matrix

Given a matrix in which the elements are sorted rowwise and columnwise.
We need to search for a given target element in the matrix.
If we traverse through the whole matrix we will need O(m*n) time but we need to take a different approach.
"""


# O(N+M) time / O(1) space
# where N :length of a row, M:length of a column
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]
