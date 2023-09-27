#!/usr/bin/python3

def rain(walls):
    """
    Calculate the amount of rainwater that can be retained between walls.

    Args:
        walls (list[int]): A list of non-negative integers representing wall heights.

    Returns:
        int: The total amount of rainwater retained.

    This function calculates the amount of rainwater that can be retained between walls
    by finding the maximum height of walls to the left and right of each position and
    determining the water that can be trapped at each position.

    Assumptions:
    - The ends of the list (before index 0 and after index walls[-1]) are not walls,
      meaning they will not retain water.
    - If the list is empty, it returns 0.
    """

    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = walls[0]
    right_max[n - 1] = walls[n - 1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(n):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water

if __name__ == "__main__":
    # Test cases
    print(rain([]))  # Correct output: 0
    print(rain([2, 0, 2]))  # Correct output: 2
    print(rain([0, 1, 0, 2, 0, 3, 0, 4]))  # Correct output: 6
    print(rain([1, 1, 2, 0, 1, 1, 1]))  # Correct output: 0
    print(rain([0, 2, 1, 0, 1, 3, 1, 2, 1, 1, 2, 1]))  # Correct output: 7
    print(rain([2, 0, 0, 0, 0, 3, 0]))  # Correct output: 6
    print(rain([1]))  # Correct output: 0
    print(rain([3, 3]))  # Correct output: 0