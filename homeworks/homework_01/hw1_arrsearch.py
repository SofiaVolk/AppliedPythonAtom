#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    global first, second
    d = dict()
    k1 = []
    k2 = []
    c = 0
    if len(input_list) > 1:
        for position, value in enumerate(input_list):
            raznost = n - value
            d[raznost] = position

        for j, val in enumerate(input_list):
            s = d.get(val, -1)
            if j == s:
                continue
            else:
                if s != -1:
                    if isinstance(s, list):
                        first = s[0]
                        second = s[1]
                        break
                    else:
                        first = s
                        s = d.get(n - val, -1)
                        if isinstance(s, list):
                            second = s[0]
                        else:
                            second = s
                        break
                else:
                    continue
        if s == -1:
            return None
        else:
            return first, second
    else:
        return None
