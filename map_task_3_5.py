def map_task_3_5(people):
    """
    Extract names from a list of dictionaries.
    Args:
        people: list of dictionaries [{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}]
    Returns:
        list of names
    """
    return list(map(lambda i: i['name'],people))
a=[{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}]
print(map_task_3_5(a))
