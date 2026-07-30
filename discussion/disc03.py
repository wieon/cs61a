import math

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 0:
        return 1
    else:
        return n * skip_factorial(n-2)


def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(283)
    3
    8
    2
    8
    3
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n%10)
        swipe(n//10)
        print(n%10)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(9)
    False
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 2:
        return True
    def helper(k):
        if k >= math.sqrt(n):
            return (n%k != 0)
        elif n%k == 0:
            return False
        return (n%k != 0) & helper(k+1)
    
    return helper(2)


""" 若将helper()函数定义在is_prime()函数外面 """
def is_prime_helper(n, k):
    if k >= math.sqrt(n):
        return (n%k != 0)
    elif n%k == 0:
        return False
    return (n%k != 0) & is_prime_helper(n, k+1)

def is_prime2(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(9)
    False
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    return is_prime_helper(n, 2)


def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1 + hailstone(n//2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return 1 + hailstone(n*3+1)


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 2012 and t = 2, we have that the subsequences are
        2
        0
        1
        2
        20
        21
        22
        01
        02
        12
    and of these, the maximum number is 22, so our answer is 22.

    >>> max_subseq(2012, 2)
    22
    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    if t == 0 or n == 0:
        return 0
    else:
        with_last = max_subseq(n//10, t-1) * 10 + n%10
        without_last = max_subseq(n//10, t)
        return max(with_last, without_last)



def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) == True or i%7 == 0:
            direction = -direction
        if direction == 1 and who == 5:
            return f(i+1, 1, direction)
        elif direction == 1 and who != 5:
            return f(i+1, who+1, direction)
        elif direction == -1 and who == 1:
            return f(i+1, 5, direction)
        elif direction == -1 and who != 1:
            return f(i+1, who-1, direction)

    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
    
print(sevens(18, 5))