#!/usr/bin/python3
"""
Determining the winner of a game of prime numbers
"""


def isWinner(x, nums):
    """
    returns the winner
    """
    def sieve_of_eratosthenes(n):
        """
        Finds all primes smaller than n
        """
        prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if prime[p] is True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        set_of_prime = set()
        for p in range(2, n + 1):
            if prime[p] is True:
                set_of_prime.add(p)
        return set_of_prime

    max_num = max(nums)
    set_of_prime = sieve_of_eratosthenes(max_num)

    def prime_game(n):
        """
        Simulates the game and returns the winner
        """
        if n < 2:
            return "Ben"
        primes = [prime for prime in set_of_prime if prime <= n]
        if not primes:
            return "Ben"

        player = 0
        available = [True] * (n + 1)

        for p in primes:
            if available[p]:
                player = 1 - player
                for i in range(p, n + 1, p):
                    available[i] = False

        if player == 0:
            return "Maria"

        return "Ben"

    if nums:
        marias = 0
        bens = 0

        for n in nums:
            winner = prime_game(n)
            if winner == "Ben":
                bens += 1
            else:
                marias += 1

        if bens > marias:
            return "Ben"
        if marias > bens:
            return "Maria"

    return None
