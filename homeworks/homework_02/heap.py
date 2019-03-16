#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.array = array[:]
        self.build_heap()

    def add(self, elem_with_priority):
        self.array.append(elem_with_priority)
        heap_size = len(self.array) - 1
        self.el_up(heap_size)

    def el_up(self, i):
        parent = i // 2
        # новый элемент не больше корня и новый элемент больше родителя
        while i >= 1 and comparator_d(self.array[i], self.array[parent]):
            self.array[parent], self.array[i] = \
                self.array[i], self.array[parent]
            i = parent
            parent = (i - 1) // 2

    def el_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        max_index = i
        heap_size = len(self.array) - 1
        if left <= heap_size and self.array[left] > self.array[max_index]:
            max_index = left
        if right <= heap_size and self.array[right] > self.array[max_index]:
            max_index = right
        if max_index != i:
            self.array[i], self.array[max_index] = \
                self.array[max_index], self.array[i]
            self.el_down(max_index)

    def build_heap(self):
        heap_size = len(self.array)
        for i in range(heap_size, -1, -1):
            self.el_down(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super(MaxHeap, self).__init__(array)

    def extract_maximum(self):
        result = tuple()
        if len(self.array):
            result = self.array.pop(0)
            self.build_heap()
        return result


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
