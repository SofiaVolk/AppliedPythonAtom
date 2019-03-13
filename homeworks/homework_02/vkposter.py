#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.friends = dict()
        self.read_post = dict()
        self.posted_post = dict()

    def user_posted_post(self, user_id: int, post_id: int):
        if user_id in self.posted_post.keys():
            self.posted_post[user_id].append(post_id)
        else:
            self.posted_post[user_id] = [post_id]

    def user_read_post(self, user_id: int, post_id: int):
        if post_id in self.read_post.keys():
            if user_id not in self.read_post[post_id]:
                self.read_post[post_id].append(user_id)
        else:
            self.read_post[post_id] = [user_id]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id != followee_user_id:
            if follower_user_id in self.friends.keys():
                self.friends[follower_user_id].append(followee_user_id)
            else:
                self.friends[follower_user_id] = [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int) -> list:
        all_posts = []
        following = self.friends.get(user_id, -1)
        if following != -1:
            for u_id in following:
                posts_u_id = self.posted_post.get(u_id, -1)
                if posts_u_id != -1:
                    all_posts.append(posts_u_id)
            ll = FastSortedListMerger()
        return ll.merge_first_k(all_posts, k)

    def get_most_popular_posts(self, k: int) -> list:
        '''
        popular_posts= []
        mh = MaxHeap(popular_posts)
        for key, value in self.read_post.items():
            mh.add((len(value), key))
        for i in range(k):
            popular_posts.append(mh.extract_maximum()[1])
        return popular_posts
        '''
        popular_posts = sorted(self.read_post, reverse=True)
        return sorted(popular_posts, key=lambda pp_id:
                      len(self.read_post[pp_id]), reverse=True)[:k]
