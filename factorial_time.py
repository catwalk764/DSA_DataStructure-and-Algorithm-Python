#!/usr/bin/env python3

import itertools
def factorial(s):
    return list(itertools.permutations(s))

s = "ABC"
print(factorial(s))