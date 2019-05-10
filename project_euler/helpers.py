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
