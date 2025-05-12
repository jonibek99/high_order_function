def min_task_1_4(dictionaries):
    """
    Find the dictionary with the smallest value.
    Args:
        dictionaries: list of dictionaries [{'a': 5}, {'a': 3}, {'a': 7}]
    Returns:
        dictionary with smallest value
    """
    return min(list(map(lambda i: i['a'],dictionaries)))
a= [{'a': 5}, {'a': 3}, {'a': 7}]
print(min_task_1_4((a)))
