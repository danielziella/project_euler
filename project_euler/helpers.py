#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import functools
import operator
import itertools


def sum_integers(n):
    return n*(n+1)//2


def sum_squares(n):
    return (2*n**3+3*n**2+n)//6


def take_last(x):
    return functools.reduce(lambda a, b: b, x)


def take_leading(x, n):
    return map(operator.itemgetter(1),
               itertools.takewhile(lambda x: x[0] < n, enumerate(x)))


def take_nth(x, n):
    return take_last(take_leading(x, n))


def cheap_prime_candidate_generator():
    yield 2
    yield 3
    n = 1
    while True:
        yield 6*n-1
        yield 6*n+1
        n = n+1


def prime_generator():
    primes = []
    for candidate in cheap_prime_candidate_generator():
        if all(candidate % x != 0 for x in primes if x <= candidate//x):
            primes.append(candidate)
            yield candidate


def factorize(n):
    factorization = {}
    for p in itertools.takewhile(lambda x: x <= n // x,
                                 cheap_prime_candidate_generator()):
        while n % p == 0:
            factorization[p] = factorization.get(p, 0)+1
            n = n // p
    if n != 1:
        factorization[n] = factorization.get(n, 0)+1
    return factorization


def combinatorial(n,k):
    return combinatorial(n-1,k-1)*n//k if k>0 else 1
