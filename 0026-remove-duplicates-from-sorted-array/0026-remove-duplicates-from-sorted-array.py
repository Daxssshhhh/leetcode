class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while (i<len(nums)):
            j = i + 1
            while(j<len(nums) and nums[i]==nums[j]):
                nums.pop(j)
            i = j
        """
        :type nums: List[int]
        :rtype: int
        """
        