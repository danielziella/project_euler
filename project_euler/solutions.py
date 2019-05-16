#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import functools
import heapq
from . import helpers
import itertools
import math
import operator
import pkg_resources


def problem1():
    """If we list all the natural numbers below 10 that are multiples of 3 or
    5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
    all the multiples of 3 or 5 below 1000."""
    return sum(x for x in range(1000) if (x % 3 == 0) or (x % 5 == 0))


def problem2():
    """Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be:
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms."""

    def fn_generator(limit):
        previous = 1
        current = 1
        while current < limit:
            yield current
            previous, current = current, previous+current

    return sum(x for x in fn_generator(4000000) if x % 2 == 0)


def problem3():
    """The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?"""

    n = 600851475143
    m = 2

    while m < n:
        while n % m == 0:
            n = n // m
        m = m+1
    return n


def problem4():
    """A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the
    largest palindrome made from the product of two 3-digit numbers."""

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    left, right = 999, 999
    product = -left*right
    h = []
    s = set()

    while not is_palindrome(-product):
        product = -(left-1)*right
        if product not in s:
            heapq.heappush(h, (product, left-1, right))
            s.add(product)
        product = -left*(right-1)
        if product not in s:
            heapq.heappush(h, (product, left, right-1))
            s.add(product)
        product, left, right = heapq.heappop(h)

    return -product


def problem5():
    """2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder. What is the smallest positive number
    that is evenly divisible by all of the numbers from 1 to 20?"""

    def lcm_generator():
        lcm = 1
        n = 0
        while True:
            n = n+1
            lcm = lcm*n//math.gcd(lcm, n)
            yield lcm
    return helpers.take_nth(lcm_generator(), 20)


def problem6():
    """The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.

    return helpers.sum_integers(100)**2 - helpers.sum_squares(100)"""


def problem7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.
    What is the 10 001st prime number?"""

    return helpers.take_nth(helpers.prime_generator(), 10001)


def problem8():
    """The four adjacent digits in the 1000-digit number that have the greatest
    product are 9 × 9 × 8 × 9 = 5832.

    < resources/problem8.txt >

    Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product. What is the value of this product?"""

    astring = pkg_resources.resource_string('project_euler.resources',
                                            'problem8.txt') \
        .decode('utf-8').replace('\n', '')

    return max([functools.reduce(operator.mul, map(int, astring[k:k+13]))
                for k in range(len(astring))])


def problem9():
    """A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,
        a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""

    for a in range(1, 1000):
        for b in range(1, a+1):
            if a**2 + b**2 == (1000 - a - b)**2:
                return a*b*(1000 - a - b)


def problem10():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    return sum(itertools.takewhile(lambda x: x < 2000000,
                                   helpers.prime_generator()))


def problem11():
    """

    In the 20×20 grid below, four numbers along a diagonal line have been
    marked in red.

    < resources/problem11.txt >

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?
    """
    astring = pkg_resources.resource_string('project_euler.resources',
                                            'problem11.txt').decode('utf-8')
    grid = list(map(lambda x: list(map(int, x.split(' '))),
                    astring.strip().split('\n')))

    n = len(grid)  # 20x20 grid

    bestrow = max(functools.reduce(operator.mul, grid[i][j:j+4])
                  for i in range(n) for j in range(n-4))
    bestcol = max(functools.reduce(operator.mul,
                                   (grid[i+k][j] for k in range(4)))
                  for i in range(n-4) for j in range(n-4))
    bestdiag1 = max(functools.reduce(operator.mul,
                                     (grid[i+k][j+k] for k in range(4)))
                    for i in range(n-4) for j in range(n-4))
    bestdiag2 = max(functools.reduce(operator.mul,
                                     (grid[i+k][j+3-k] for k in range(4)))
                    for i in range(n-4) for j in range(n-4))
    return max(bestrow, bestcol, bestdiag1, bestdiag2)


def problem12():
    """The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred
    divisors?"""
    n = 1
    divisors = 1
    while divisors <= 500:
        n = n+1
        factorization = helpers.factorize(n)
        factorization.update(helpers.factorize(n+1))
        factorization[2] = factorization[2]-1
        divisors = functools.reduce(operator.mul,
                                    map(lambda x: x+1, factorization.values()))
    return n*(n+1)//2


def problem13():
    """
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.

    < resources/problem13.txt >
    """
    astring = pkg_resources.resource_string('project_euler.resources',
                                            'problem13.txt').decode('utf-8')
    return str(sum(map(int, astring.strip().split('\n'))))[:10]


def problem14():
    """The following iterative sequence is defined for the set of positive
    integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    def collatz_step(n):
        return n // 2 if n % 2 == 0 else 3*n+1

    collatz_len = {1: 0}

    for n in range(2, 1000000):
        seq = [n]
        seq_next = collatz_step(n)
        while seq_next not in collatz_len:
            seq.append(seq_next)
            seq_next = collatz_step(seq_next)
        while len(seq) > 0:
            collatz_len[seq[-1]] = collatz_len[seq_next] + 1
            seq_next = seq.pop()
    return collatz_len


def problem15():
    """
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.
    How many such routes are there through a 20×20 grid?"""
    return helpers.combinatorial(40,20)


def problem16():
    """2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
    """
    return sum(map(int, str(2**1000)))


def problem17():
    """If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage."""
    astring = pkg_resources.resource_string('project_euler.resources',
                                            'problem17.txt').decode('utf-8')

    adict = {int(k): v for k, v in map(lambda x: x.split(':'),
                                       astring.strip().split('\n'))}

    def num_to_str(n):
        assert n < 1000000, 'n must be less than one million'

        if n >= 1000:
            return num_to_str(n//1000) + 'thousand' + \
               num_to_str(n % 1000)
        elif n >= 100:
            return num_to_str(n//100) + 'hundred' + \
               ('and' + num_to_str(n % 100) if n % 100 > 0 else '')
        elif n >= 20:
            return adict[n//10*10] + \
               num_to_str(n % 10)
        else:
            return adict[n]

    return sum(len(num_to_str(n)) for n in range(1001))


def _best_sum_over_pyramid(resource_filename):
    astring = pkg_resources.resource_string('project_euler.resources',
                                            resource_filename).decode('utf-8')

    pyramid = list(map(lambda x: list(map(int, x.split(' '))),
                       astring.strip().split('\n')))

    best_sum = pyramid[0]

    for k, row in enumerate(pyramid[1:]):
        best_sum = [max(a+c, b+c) for a, b, c in
                    zip([0]+best_sum, best_sum+[0], row)]

    return max(best_sum)




def problem18():
    """By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.
       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    < resources/problem18.txt >

    NOTE: As there are only 16384 routes, it is possible to solve this problem
    by trying every route. However, Problem 67, is the same challenge with a
    triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)"""
    return _best_sum_over_pyramid('problem18.txt')


def problem67():
    """By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.
       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and
    'Save Link/Target As...'), a 15K text file containing a triangle with
    one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not
    possible to try every route to solve this problem, as there are 2^99
    altogether! If you could check one trillion (10^12) routes every second
    it would take over twenty billion years to check them all. There is an
    efficient algorithm to solve it. ;o)
    """
    return _best_sum_over_pyramid('problem67.txt')
