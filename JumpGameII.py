class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max_jump, current_max_jump = 0, 0
        i, njump = 0, 0

        while current_max_jump<len(nums)-1:
            while i<=last_max_jump:
                current_max_jump = max(current_max_jump,nums[i]+i)
                i+=1
            if last_max_jump==current_max_jump: return False
            last_max_jump = current_max_jump

            njump+=1

        return True



test = Solution()
print test.jump([5,3,1,1,1,4])