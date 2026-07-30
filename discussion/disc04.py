# Using for loops
# def even_weighted_loop(s):
#     """
#     >>> x = [1, 2, 3, 4, 5, 6]
#     >>> even_weighted_loop(x)
#     [0, 6, 20]
#     """
#     "*** YOUR CODE HERE ***"
#     new_s = []
#     for i in range(len(s)):
#         if i%2 == 0:
#             new_s = new_s + [i * s[i]]
#     return new_s

# Using a list comprehension
def even_weighted_loop(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    return [s.index(i) * i for i in s[::2]]


print(even_weighted_loop([1, 2, 3, 4, 5, 6]))
