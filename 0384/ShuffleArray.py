import random


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        return sorted(self.nums, key=lambda x: random.random())