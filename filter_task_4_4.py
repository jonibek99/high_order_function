def filter_task_4_4(names):
    """
    Filter names that start with "A".
    Args:
        names: list of strings ["Alice", "Bob", "Anna", "Charlie"]
    Returns:
        list of names that start with "A"
    """
    return list(filter(lambda x: x[0]=='A',names))
a=["Alice", "Bob", "Anna", "Charlie"]
print(filter_task_4_4(a))
