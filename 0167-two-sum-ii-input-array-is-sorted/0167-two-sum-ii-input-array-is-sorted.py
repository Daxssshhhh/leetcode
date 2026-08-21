class Solution(object):
    def twoSum(self, numbers, target):
        l,r = 0,len(numbers)-1

        while l<r:
            currentsum=numbers[l]+numbers[r]
            if currentsum>target:
                r=r-1
            elif currentsum<target:
                l=l+1
            else:
                return[l+1,r+1]
        
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        