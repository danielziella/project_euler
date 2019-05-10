#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import heapq
from . import helpers
import math


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
    def lcm_generator():
        lcm = 1
        n = 0
        while True:
            n = n+1
            lcm = lcm*n//math.gcd(lcm, n)
            yield lcm
    return helpers.take_nth(lcm_generator(), 20)


def problem6():
    return helpers.sum_integers(100)**2 - helpers.sum_squares(100)


def problem7():
    return helpers.take_nth(helpers.prime_generator(), 10001)
