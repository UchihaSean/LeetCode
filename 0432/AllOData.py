class LinkNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = LinkNode("", 0)
        self.head.nxt = LinkNode("", float("inf"))
        self.tail = self.head.nxt
        self.tail.prev = self.head
        self.kvdict = {}  # key:node
        self.vkdict = {}  # node.val: [leftnode,rightnode]

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.kvdict:
            new = LinkNode(key, 1)
            self.kvdict[key] = new
            if 1 not in self.vkdict:
                self.vkdict[1] = [new, new]
            else:
                self.vkdict[1][0] = new
            self.head.nxt.prev, self.head.nxt, new.nxt, new.prev = new, new, self.head.nxt, self.head
        else:
            alter = self.kvdict[key]
            left, right = self.vkdict[alter.val]
            if alter == left or alter == right:
                if alter == left == right:
                    right = right.prev
                    left = left.nxt
                    self.vkdict.pop(alter.val)
                elif alter == left:
                    left = left.nxt
                    self.vkdict[alter.val][0] = left
                elif alter == right:
                    right = right.prev
                    self.vkdict[alter.val][1] = right

            alter.prev.nxt, alter.nxt.prev = alter.nxt, alter.prev
            alter.val += 1
            if alter.val in self.vkdict:
                left = self.vkdict[alter.val][0]
                self.vkdict[alter.val][0] = alter
                left.prev.nxt, left.prev, alter.prev, alter.nxt = alter, alter, left.prev, left
            else:
                self.vkdict[alter.val] = [alter, alter]
                right.nxt.prev, right.nxt, alter.prev, alter.nxt = alter, alter, right, right.nxt

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.kvdict:
            alter = self.kvdict[key]
            left, right = self.vkdict[alter.val]
            if alter == left or alter == right:
                if alter == left == right:
                    left = left.nxt
                    right = right.prev
                    self.vkdict.pop(alter.val)
                elif alter == left:
                    left = left.nxt
                    self.vkdict[alter.val][0] = alter.nxt
                elif alter == right:
                    right = right.prev
                    self.vkdict[alter.val][1] = alter.prev
            alter.prev.nxt, alter.nxt.prev = alter.nxt, alter.prev
            alter.val -= 1
            if alter.val == 0:
                self.kvdict.pop(key)
            else:
                if alter.val in self.vkdict:
                    right = self.vkdict[alter.val][1]
                    self.vkdict[alter.val][1] = alter
                    right.nxt.prev, right.nxt, alter.prev, alter.nxt = alter, alter, right, right.nxt
                else:
                    self.vkdict[alter.val] = [alter, alter]
                    left.prev.nxt, left.prev, alter.prev, alter.nxt = alter, alter, left.prev, left

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail.prev.val == 0:
            return ""
        else:
            return self.tail.prev.key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.nxt.val == float("inf"):
            return ""
        else:
            return self.head.nxt.key