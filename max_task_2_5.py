def max_task_2_5(people):
    """
    Find the person with the highest age.
    Args:
        people: list of dictionaries [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}]
    Returns:
        dictionary of person with highest age
    """
    a=list(map(lambda i: i['age'],people))
    return max(a)
v=[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}]
print(max_task_2_5(v))