#!/usr/bin/env python
# coding: utf-8
from collections import Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.action = {}

    def register_event(self, user_id, time):
        if user_id in self.action.keys():
            self.action[user_id].append(time)
        else:
            self.action[user_id] = [time]

    def query(self, count, time):
        users = []
        time_end = time - self.FIVE_MIN
        users = set([i for i in self.action.keys() if len(self.action[i]) == count
                     for j in self.action[i] if time_end < j < time])
        return len(users)
