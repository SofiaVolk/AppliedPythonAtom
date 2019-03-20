#!/usr/bin/env python
# coding: utf-8
import time
from collections import OrderedDict


class LRUCacheDecorator:

    def __init__(self, maxsize=None, ttl=None):
        self.maxsize = maxsize
        self.ttl = ttl
        self.function_result = OrderedDict()
        self.time_in_cache = OrderedDict()

    def del_old(self, *args):
        self.function_result.popitem(*args)
        self.time_in_cache.popitem(*args)

    def update_cache(self, arg, result):
        self.function_result[arg] = result
        self.time_in_cache[arg] = time.time()

    def __call__(self, some_function):
        def lru_function(*args, **kwargs):
            input_param = args

            # если элемент есть в кэше
            if self.function_result.get(input_param):
                if self.ttl is not None:
                    if self.ttl > (time.time() - self.time_in_cache[input_param]):
                        return self.function_result[input_param]
                    else:
                        self.del_old(input_param)
                        new_result = some_function(*args, **kwargs)
                        self.update_cache(input_param, new_result)
                        return new_result
                else:
                    return self.function_result[input_param]

            # если элемента в кэше нет, то проверяем забит ли кэш (можно ли его туда
            # положить или нужно удалить самый старый элемент кэша)
            elif self.maxsize != len(self.function_result):
                new_result = some_function(*args, **kwargs)
                self.update_cache(input_param, new_result)
                return new_result
            else:
                # освобождаем место, удаляя самый старый элемент, даже если его время меньше ttl
                self.del_old()
                new_result = some_function(*args, **kwargs)
                self.update_cache(input_param, new_result)
                return new_result

        return lru_function
