#!/usr/bin/python3
"""
Prime Game
"""

def sieve_of_eratosthenes(max_num):
    """
    Uses the Sieve of Eratosthenes to find all prime numbers up to max_num.
    """
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(max_num ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return sieve


def count_prime_moves(n, sieve):
    """
    Counts the number of moves that can be made in a game of size n.
    A move is made when a prime number and its multiples are removed.
    """
    moves = 0
    removed = set()

    for i in range(2, n + 1):
        if sieve[i] and i not in removed:
            moves += 1
            # Mark all multiples of this prime as removed
            for multiple in range(i, n + 1, i):
                removed.add(multiple)

    return moves


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    sieve = sieve_of_eratosthenes(max_num)

    players = {'Maria': 0, 'Ben': 0}

    for n in nums:
        moves = count_prime_moves(n, sieve)

        if moves % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None

