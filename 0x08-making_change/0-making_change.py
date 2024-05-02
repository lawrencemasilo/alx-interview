#!/usr/bin/python3
"""
Solves the rotate 2D problem.
"""


def makeChange(coins, total):
    """
    Returns the minimum number of coins needed to reach the total.
    """
    if total <= 0:
        return 0

    min_num = [float('inf')] * (total + 1)
    min_num[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_num[i] = min(min_num[i], min_num[i - coin] + 1)

    if min_num[total] == float('inf'):
        return -1
    return min_num[total]
