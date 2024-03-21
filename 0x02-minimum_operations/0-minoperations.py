#!/usr/bin/python3

"""
This method calculates the fewest number of operations needed to result in
exactly n H characters in a file.
"""


def minOperations(n):
    """
    returns total numnber of operations needed.
    """
    if n > 1:
        total_num = 0
        factors_array = []
        divisor = 2
        while n > 1:
            if n % divisor != 0:
                divisor = divisor + 1
            else:
                factors_array.append(divisor)
                n = n // divisor

        for factor in factors_array:
            total_num = total_num + factor

        return total_num

    return 0
