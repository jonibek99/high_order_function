def max_task_2_2(words):
    """
    Find the longest word.
    Args:
        words: list of strings ["pen", "notebook", "eraser"]
    Returns:
        longest word
    """
    a=max(words,key=lambda i: len(i))
    return a
p=["pen", "notebook", "eraser"]
print(max_task_2_2(p))
