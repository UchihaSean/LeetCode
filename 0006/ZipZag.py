class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1: return s
        order_str=[]
        for i in range(numRows): order_str.append([])
        index =0
        direct =0
        for i in range(len(s)):
            order_str[index].append(s[i])
            if direct==0: index+=1
            if direct==1: index-=1
            if index==-1:
                direct=0
                index=1
            if index==numRows:
                direct=1
                index=numRows-2
        convert_string=""
        for i in range(len(order_str)):
            for j in range(len(order_str[i])):
                convert_string+=order_str[i][j]

        return convert_string



test = Solution()
print test.convert("ABC", 1)