class trie:
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.end = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = trie(0)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = trie(c)
            node = node.child[c]
        node.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.child:
                return False
            node = node.child[c]
        return node.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.child:
                return False
            node = node.child[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)