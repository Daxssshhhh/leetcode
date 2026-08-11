class Solution(object):
    def removeElement(self, nums, val):
        i = 0 
        while (i<len(nums)):
            if(nums[i]==val):
                nums.pop(i)
            else:
                i = i + 1
        return len(nums)
            
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        