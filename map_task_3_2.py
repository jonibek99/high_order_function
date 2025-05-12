def map_task_3_2(words):
    """
    Convert all words to uppercase.
    Args:
        words: list of strings ["cat", "dog", "fish"]
    Returns:
        list of uppercase words
    """
    return list(map(lambda i : i.upper(),words))
a=["cat", "dog", "fish"]
print(map_task_3_2(a))
