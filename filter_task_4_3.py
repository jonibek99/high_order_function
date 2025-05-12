def filter_task_4_3(numbers):
    """
    Keep numbers greater than 10.
    Args:
        numbers: list of integers [5, 11, 20, 7, 10]
    Returns:
        list of numbers greater than 10
    """
    return list(filter( lambda i: i>10,numbers))
print(filter_task_4_3([5, 11, 20, 7, 10]))
