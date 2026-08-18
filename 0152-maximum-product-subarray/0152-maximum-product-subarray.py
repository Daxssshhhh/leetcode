class Solution(object):
    def maxProduct(self, nums):
        result = max(nums)
        curmax,curmin=1,1
        for n in nums:
            if n == 0:
                curmax,curmin=1,1
                continue
            tmp = n*curmax
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(tmp,n*curmin,n)
            result = max(curmax,result)
        return result


        """
        :type nums: List[int]
        :rtype: int
        """
        