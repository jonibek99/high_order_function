def lambda_task_5_1(numbers):
    """
    Sort the numbers in descending order.
    Args:
        numbers: list of integers [3, 1, 4, 2]
    Returns:
        sorted list in descending order
    """
    return sorted(numbers)[::-1]
a=[3, 1, 4, 2]
print(lambda_task_5_1(a))