class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        dict={}
        dupli={}
        list=[]
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        # print dict
        for i in range(len(nums)):
            for j in range(i):
                dict[nums[i]]-=1
                dict[nums[j]]-=1
                third= -nums[i]-nums[j]
                # print nums[i],nums[j],third
                if third in dict and dict[third]>0:
                    now = []
                    now.append(max(nums[i],nums[j],third))
                    now.append(min(nums[i],nums[j],third))
                    now.append(-now[0]-now[1])
                    list.append(now)

                dict[nums[i]]+=1
                dict[nums[j]]+=1

        return map(list,list)


test = Solution()
print test.threeSum([-1, 0, 1, 2, -1, -4])