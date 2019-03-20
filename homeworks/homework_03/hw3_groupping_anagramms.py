#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    result = {}

    if not words:
        return words

    for word in words:
        anagramm = str(sorted(word.lower()))
        if anagramm in result.keys():
            result[anagramm].append(word)
        else:
            result[anagramm] = [word]
    return result.values()
