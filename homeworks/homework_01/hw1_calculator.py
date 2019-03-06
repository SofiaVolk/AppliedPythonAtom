#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    c = 0
    if operator == 'plus':
        if isinstance(x, (float, int)) and isinstance(y, (float, int)):
            c = x+y
        else:
            return None
        return c
    elif operator == 'minus':
        if isinstance(x, (float, int)) and isinstance(y, (float, int)):
            c = x-y
        else:
            return None
        return c
    elif operator == 'mult':
        if isinstance(x, (float, int)) and isinstance(y, (float, int)):
            c = x*y
        else:
            return None
        return c
    elif operator == 'divide':
        if (y == 0):
            return None
        else:
            if isinstance(x, (float, int)) and isinstance(y, (float, int)):
                c = x / y
            else:
                return None
            return c
    else:
        return None
