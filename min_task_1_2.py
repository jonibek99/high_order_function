def min_task_1_2(words):
    """
    Find the shortest word.
    Args:
        words: list of strings ["apple", "banana", "kiwi", "pear"]
    Returns:
        shortest word
    """
    a=list(map(lambda i: len(i),words))
    b=min(a)
    c=a.index(b)
    return c
p=["apple", "banana", "kiwi", "pear"]
print(min_task_1_2(p))