def filter_task_4_5(students):
    """
    Filter students who passed (grade >= 60).
    Args:
        students: list of dictionaries [{"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 55}, {"name": "Charlie", "grade": 70}]
    Returns:
        list of students who passed
    """
    return dict(filter(lambda i : i['grade'] >=60 ,students))
a=[{"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 55}, {"name": "Charlie", "grade": 70}]
print(filter_task_4_5(a))
