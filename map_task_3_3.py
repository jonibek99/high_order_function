def map_task_3_3(words):
    """
    Get the lengths of each word.
    Args:
        words: list of strings ["hi", "hello", "bye"]
    Returns:
        list of word lengths
    """
    return list(map(lambda i: len(i) ,words))
a=["hi", "hello", "bye"]
print(map_task_3_3(a))
