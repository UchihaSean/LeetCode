class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sumGasCost = []
        for i in range(len(gas)):
            if i==0:
                sumGasCost.append(gas[i]-cost[i])
            else:
                sumGasCost.append(sumGasCost[-1]+gas[i]-cost[i])
        minSumGasCost = 99999999
        minIndex = -1
        for i in range(len(sumGasCost)):
            if sumGasCost[i]<minSumGasCost:
                minSumGasCost=sumGasCost[i]
                minIndex = i

        # print minIndex
        sumCost = 0
        for i in range(len(gas)):
            index = (minIndex+i+1) % len(gas)
            sumCost+=gas[index] - cost[index]
            if sumCost<0: return -1

        return (minIndex+1) % len(gas)

test = Solution()
print test.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
