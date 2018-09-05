class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=len(nums1)+len(nums2)
        return (findKth(nums1,nums2,l/2)+findKth(nums1,nums2,(l-1)/2))/2.0


def findKth(x,y,k):
    if len(x)>len(y): x,y=y,x
    if not x: return y[k]
    if k==len(x)+len(y)-1: return max(x[-1],y[-1])
    i= len(x)/2
    j=k-i
    if x[i]<y[j]:
        return findKth(x[i:],y[:j],j)
    else:
        return findKth(x[:i],y[j:],i)






test = Solution()

print test.findMedianSortedArrays([1],[2,3,4,5,6,7,8])