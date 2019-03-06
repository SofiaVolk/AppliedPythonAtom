#!/usr/bin/env python
# coding: utf-8


def det2(matrix):
    o = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return o


def minor(matrix, i, j):
            tmp = [row for k, row in enumerate(matrix) if k != i]
            tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
            return tmp


def calculate_determinant(list_of_lists):
    summ = 0
    try:
        size = len(list_of_lists)
        o = 0
        ss = len(list_of_lists[0])
        if size == 2:
            return det2(list_of_lists)
        if size == 1 and ss == 1:
                return list_of_lists[0][0]
        for j in range(size):
                o = (-1) ** j * list_of_lists[0][j] *\
                    calculate_determinant(minor(list_of_lists, 0, j))
                summ = summ + o
        return float(summ)
    except IndexError:
        return None
    except TypeError:
        return None
