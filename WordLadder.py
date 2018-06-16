class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.word_path = []
        self.shortest_path_len = 9999999
        self.end_word = endWord
        self.word_list = set(wordList)

        self.dfs([beginWord])

        return self.word_path



    def dfs(self,word_path):
        """
        search the path from begin to end
        """
        "word path length larger than shorest one, cut"
        if len(word_path)>self.shortest_path_len: return None

        "end word found"
        if word_path[-1] == self.end_word:
            if len(word_path)<self.shortest_path_len:
                self.shortest_path_len = len(word_path)
                self.word_path=[word_path[:]]
            elif len(word_path) == self.shortest_path_len:
                self.word_path.append(word_path[:])
            return None

        "search for next word"
        word = word_path[-1]
        for i in range(len(self.end_word)):
            new_word = word[:i]+self.end_word[i] + word[i+1:]
            if new_word in word_path or new_word not in self.word_list: continue
            word_path.append(new_word)
            self.dfs(word_path)
            word_path.pop()

        for char in "abcdefghijklmnopqrstuvwxyz":
            for i in range(len(word)):
                new_word = word[:i]+char+word[i+1:]
                if new_word in word_path or new_word not in self.word_list or char==self.end_word[i]: continue
                word_path.append(new_word)
                self.dfs(word_path)
                word_path.pop()








test = Solution()
print test.findLadders("hit","cog",["hot","dot","dog","lot","log","cog"])
