class TrieNode(object):
    def __init__(self, val=None):
        self.val = val
        self.is_end = False
        self.child = {}


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c in node.child:
                node = node.child[c]
            else:
                new_node = TrieNode(c)
                node.child[c] = new_node
                node = new_node
        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = [self.root]
        for c in word:
            if c == '.':
                node = [child for t in node for child in t.child.values()]
            else:
                node = [t.child[c] for t in node if c in t.child]
        return any(t.is_end for t in node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)