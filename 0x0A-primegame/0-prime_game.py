#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """
    Use the Sieve of Eratosthenes to find all primes up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i]]


def play_game(n):
    """
    Simulate one round of the game for a given n.
    Returns the number of primes chosen in that round.
    """
    primes = sieve_of_eratosthenes(n)
    multiples_removed = set()
    turn_count = 0

    for prime in primes:
        if prime not in multiples_removed:
            turn_count += 1
            for multiple in range(prime, n + 1, prime):
                multiples_removed.add(multiple)

    return turn_count


def isWinner(x, nums):
    """
    Determine the overall winner after x rounds of the game.
    """
    players = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes_picked = play_game(n)
        if primes_picked % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None


# Ensure two blank lines before and after functions (PEP8 compliance).

