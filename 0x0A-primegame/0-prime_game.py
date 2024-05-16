#!/usr/bin/python3
"""
Determining the winner of a game of prime numbers
"""


def isWinner(x, nums):
    """
    returns the winner
    """

    if not nums or x < 1:
        return None

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    def determine_winner(n):
        """
        Simulates the game and returns the winner
        """

        primes = [i for i in range(2, n + 1) if is_prime[i]]
        if not primes:
            return 'Ben'

        rounds = 0
        remaining = set(range(1, n + 1))

        while primes:
            prime = primes.pop(0)
            multiples = set(range(prime, n + 1, prime))
            remaining -= multiples
            primes = [p for p in primes if p in remaining]
            rounds += 1

        if rounds % 2 == 0:
            return 'Ben'
        else:
            return 'Maria'

    ben = 0
    maria = 0

    for num in nums:
        winner = determine_winner(num)
        if winner == 'Ben':
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'

    return None
