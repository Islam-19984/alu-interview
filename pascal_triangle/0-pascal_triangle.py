#!/usr/bin/python3

def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the result list with the first row
    result = [[1]]

    for i in range(1, n):
        # Calculate the next row based on the previous row
        previous_row = result[-1]
        next_row = [1]
        for j in range(1, i):
            next_row.append(previous_row[j - 1] + previous_row[j])
        next_row.append(1)

        # Append the next row to the result
        result.append(next_row)

    return result

