def map_task_3_1(numbers):
    """
    Add 10 to each number.
    Args:
        numbers: list of integers [1, 2, 3]
    Returns:
        list with 10 added to each number
    """
    return list(map(lambda i: i+10,numbers))
a=[1, 2, 3]
print(map_task_3_1(a))
