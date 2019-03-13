import input
import os


def print_table(table):
    for i in table:
        coll = i.values()
        collk = i.keys()
        col_width = [0 for i in range(len(coll))]
        break
    for ii in table:
        coll = ii.values()
        collk = ii.keys()
        for i, x in enumerate(coll):
            len1 = len(str(x))
            if col_width[i] < len1:
                col_width[i] = len1
        for i, x in enumerate(collk):
            len1 = len(str(x))
            if col_width[i] < len1:
                col_width[i] = len1
    kee1 = []
    summ = sum(col_width)
    print("-"*(summ+20))
    for line in table:
        kee = line.keys()
        if kee != kee1:
            print("|  " + "  |  ".join("{:{}}".format
                  (' '*(int((col_width[i]-len(str(x)))/2))+x, col_width[i])
                                    for i, x in enumerate(kee)) + " | ")
        else:
            break
        kee1 = kee
    for line in table:
        values = line.values()
        print("|  " + "  |  ".join("{:{}}".
                                   format(x, col_width[i])
                                   for i, x in enumerate(values)) + " | ")
    print("-" * (summ + 20))


def table_proc(data):
    print_table(data)
