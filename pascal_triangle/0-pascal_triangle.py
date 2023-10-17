#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row and returns it as a list of lists of integers.

    Args:
    n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    list: A list of lists, each representing a row of Pascal's triangle, containing integer values.

    If n is less than or equal to 0, an empty list is returned.

    Example:
    >>> n = 5
    >>> result = pascal_triangle(n)
    >>> for row in result:
    >>>     print(row)

    Output:
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    """
    if n <= 0:
        return []

    triangle = []  # Initialize an empty list to store Pascal's triangle.
    for i in range(n):  # Iterate through each row from 0 to n-1.
        row = []  # Initialize an empty list to represent the current row.
        for j in range(i + 1):  # Iterate through each element in the current row.
            if j == 0 or j == i:
                row.append(1)  # The first and last elements in a row are always 1.
            else:
                prev_row = triangle[i - 1]  # Retrieve the previous row.
                row.append(prev_row[j - 1] + prev_row[j])  # Calculate and append the current element.
        triangle.append(row)  # Append the current row to the triangle list.

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)  # Print each row of Pascal's triangle up to the 5th row.


