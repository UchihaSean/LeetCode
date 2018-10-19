import numpy as np


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.lis = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = len(self.lis)
            self.lis.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # print(self.lis)
        # print(self.dict)
        if val in self.dict:
            index = self.dict[val]
            self.dict[self.lis[len(self.lis) - 1]] = index
            del self.dict[val]
            self.lis[index], self.lis[len(self.lis) - 1] = self.lis[len(self.lis) - 1], self.lis[index]

            self.lis.pop()
            # print(self.lis)
            # print(self.dict)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = int(np.random.random() * len(self.dict))
        # print(self.dict)
        # print(self.lis)
        # print(index)
        return self.lis[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# obj.insert(0)
# obj.remove(0)
# obj.insert(-1)
# obj.remove(0)