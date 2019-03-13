#!/usr/bin/env python
# coding: utf-8


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        out_len = []
        for i in list_of_lists:
            out_len += i
        out_len = sorted(out_len)
        return sorted(out_len[-k:], reverse=True)
