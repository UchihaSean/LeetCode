from Queue import Queue

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words: return []
        if len(words)*len(words[0])>len(s): return []
        pair = []
        words_dict={}
        for i in range(len(words)):
            words_dict[words[i]]=i
        for i in range(len(words[0])):
            words_set=set([])
            q = Queue()

            for j in range(len(words)):
                current_word = s[i+j*len(words[0]):i+(j+1)*len(words[0])]
                if current_word in words_dict:
                    words_set.add(words_dict[current_word])
                q.put(current_word)
            if len(words_set) == len(words): pair.append(i)

            j = i+ len(words)*len(words[0])
            while j+len(words[0])<len(s):
                past_word = q.get()
                if past_word in words_dict:
                    print words_set,words_dict[past_word]
                    words_set.remove(words_dict[past_word])
                current_word = s[j:j+len(words[0])]
                if current_word in words_dict:
                    words_set.add(words_dict[current_word])
                q.put(current_word)

                if len(words_set)== len(words): pair.append(j - (len(words)-1)*len(words[0]))
                j+=len(words[0])


        return pair








test = Solution()
print test.findSubstring("barfoofoobarthefoobarman",["foo","bar","the"])