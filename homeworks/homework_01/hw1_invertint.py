#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    number_inv = []
    f = 0

    if number == 0:
        return 0
    elif number < 0:
        f = 1
        number = abs(number)

    while number > 0:
        number_inv.append(number % 10)
        number = number // 10

    number_inv = int(''.join(str(i) for i in number_inv))
    if f == 0:
        return number_inv
    else:
        return -number_inv
