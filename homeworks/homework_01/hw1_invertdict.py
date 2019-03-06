#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    if isinstance(source_dict, dict):
        k1 = []
        k2 = []
        k3 = []
        k4 = []
        flag = 0
        newdict = {}
        for val in source_dict.values():
            if not isinstance(val, (int, float, str)):
                    for index, v in enumerate(val):
                        if isinstance(v, (list, tuple, set)):
                            val.extend(v)
                            val.pop(index)
        for k, v in source_dict.items():
            if isinstance(v, (list, tuple, set)):
                for item in v:
                    if item in source_dict[k]:
                        if item in newdict.keys():
                            k1.append(newdict.get(item))
                            k2 = k1
                            k1 = []
                            k2.append(k)
                            newdict[item] = k2
                        else:
                            newdict[item] = k
                k2 = []
            else:
                for i in source_dict.keys():
                    if v == source_dict[i]:
                        if v in newdict.keys():
                            k4.append(newdict.get(v))
                            k3 = k4
                            k4 = []
                            k3.append(i)
                            newdict[v] = k3
                        else:
                            newdict[v] = i

        for val in newdict.values():
            if not isinstance(val, (int, float, str)):
                    for index, v in enumerate(val):
                        if isinstance(v, (list, tuple, set)):
                            val.extend(v)
                            val.pop(index)

        return newdict
