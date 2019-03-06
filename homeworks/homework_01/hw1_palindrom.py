#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    if input_string != "":
        reverse_string = input_string[::-1]

        if input_string.lower() == reverse_string.lower():
            return True
        else:
            return False
