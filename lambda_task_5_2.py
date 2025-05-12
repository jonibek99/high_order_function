def lambda_task_5_2(words):
    """
    Sort words by their length (shortest to longest).
    Args:
        words: list of strings ["apple", "banana", "kiwi", "pear"]
    Returns:
        sorted list by word length
    """
    return sorted(words,key=lambda i: len(i))
a=["apple", "banana", "kiwi", "pear"]
print(lambda_task_5_2(a))
