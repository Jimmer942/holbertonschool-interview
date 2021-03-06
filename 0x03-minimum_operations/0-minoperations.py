#!/usr/bin/python3
"""Min ops"""


def minOperations(n):
    """Calculares the minimum number of copyall/paste operations"""
    number = 1
    copy = 0
    operations = 0
    if type(n) is not int or n < 2:
        return 0
    else:
        for i in range(n):
            if number == n:
                return operations
            elif n % number == 0:
                copy = number
                number += copy
                operations += 2
            else:
                number += copy
                operations += 1
