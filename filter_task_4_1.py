def filter_task_4_1(numbers):
    """
    Filter out even numbers.
    Args:
        numbers: list of integers [1, 2, 3, 4, 5]
    Returns:
        list of odd numbers
    """
    return list(filter(lambda i: i%2!=0,numbers ))
n=[1, 2, 3, 4, 5]
print(filter_task_4_1(n))
