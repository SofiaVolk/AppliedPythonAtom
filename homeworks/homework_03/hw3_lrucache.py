#!/usr/bin/env python
# coding: utf-8
from collections import OrderedDict
import time


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        self.maxsize = maxsize
        self.ttl = ttl
        self.lru = OrderedDict()
        self.time = OrderedDict()

    def __call__(self, f):
        def funcc(*args, **kwargs):
            if self.ttl is None:
                self.ttl = 3600000
            if self.lru.get(args[0]):
                if self.ttl > (time.time() - self.time[args[0]]):
                    return self.lru[args[0]]
                else:
                    self.lru.popitem(args[0])
                    self.time.popitem(args[0])
                    r = f(*args, **kwargs)
                    self.lru.update({args[0]: r})
                    self.time[args[0]] = time.time()
                    return r
            elif len(self.lru) == self.maxsize:
                self.lru.popitem(args[0])
                self.time.popitem(args[0])
                r = f(*args, **kwargs)
                self.lru.update({args[0]: r})
                self.time[args[0]] = time.time()
                return r
            else:
                r = f(*args, **kwargs)
                self.lru.update({args[0]: r})
                self.time[args[0]] = time.time()
                return r
        return funcc
