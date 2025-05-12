def max_task_2_4(words):
    """
    Find the word with the most vowels.
    Args:
        words: list of strings ["tree", "education", "sky", "road"]
    Returns:
        word with most vowels
    """
    c=0
    b=[]
    for i in words:
        if i in 'euioa,EUIOA':
            c+=1
            b.append(c)
    return(b)
a=["tree", "education", "sky", "road"]
print(max_task_2_4(a))



