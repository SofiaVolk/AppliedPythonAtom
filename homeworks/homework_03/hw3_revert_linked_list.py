#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    if head is None:
        return head
    tail = None
    while head:
        head.next_node, tail, head = tail, head, head.next_node
    return tail
