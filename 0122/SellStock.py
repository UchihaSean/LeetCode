class Solution(object):
    def maxProfit(self, p):
        if not p: return 0
        min_price = p[0]
        left = [0]
        right = [0]
        for i in range(len(p)):
            min_price = min(min_price,p[i])
            left.append(max(left[-1],p[i]-min_price))
        max_price = p[-1]
        for i in range(len(p)-1,-1,-1):
            max_price = max(max_price,p[i])
            right.append(max(right[-1],max_price-p[i]))
        left.remove(0)
        right.remove(0)
        max_profit = 0
        for i in range(len(p)):
            if left[i]+right[len(p)-i-1]>max_profit:
                max_profit = left[i]+right[len(p)-i-1]
        return max_profit





test = Solution()
print test.maxProfit([2,1,2,0,1])