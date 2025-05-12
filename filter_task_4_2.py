def filter_task_4_2(words):
    """
    Keep words longer than 4 letters.
    Args:
        words: list of strings ["hi", "hello", "world", "cat"]
    Returns:
        list of words longer than 4 letters
    """
    return list(filter(lambda i: len(i)>4,words))
a=["hi", "hello", "world", "cat"]
print(filter_task_4_2(a))
