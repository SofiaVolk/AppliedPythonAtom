import input
import os


def print_table(table):
    for i in table:
        col_width = [0 for ii in range(len(i))]
        break
    for ii in table:
        for i, x in enumerate(ii):
            len1 = len(str(x))
            if col_width[i] < len1:
                col_width[i] = len1
    summ = sum(col_width)
    print("-"*(summ+13))
    print("| " + " | ".join("{:{}}".format
          (' '*(int((col_width[i]-len(str(x)))/2))+x, col_width[i])
                            for i, x in enumerate(table[0])) + " | ")
    table.pop(0)
    for line in table:
        print("| " + " | ".join("{:{}}".
                                format(x, col_width[i])
                                for i, x in enumerate(line)) + "  | ")
    print("-" * (summ + 13))


def table_proc(data):
    print_table(data)
