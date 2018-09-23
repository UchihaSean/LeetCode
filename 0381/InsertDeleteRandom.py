import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lis = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.lis.append(val)
        if val in self.dict:
            self.dict[val].add(len(self.lis) - 1)
        else:
            self.dict[val] = set([len(self.lis) - 1])
        return len(self.dict[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict or not self.dict[val]: return False
        index = self.dict[val].pop()
        if index == len(self.lis) - 1:
            self.lis.pop()
            return True

        self.lis[index] = self.lis[len(self.lis) - 1]
        self.dict[self.lis[index]].remove(len(self.lis) - 1)
        self.dict[self.lis[index]].add(index)
        self.lis.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.lis[int(random.random() * len(self.lis))]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()