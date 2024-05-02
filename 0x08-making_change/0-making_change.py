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
        if coin <= total:
            min_num[coin] = 1

    max_coin_value = max(coins)
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                min_num[i] = min(min_num[i], min_num[i - coin] + 1)

    if min_num[total] == float('inf'):
        return -1
    return min_num[total]
