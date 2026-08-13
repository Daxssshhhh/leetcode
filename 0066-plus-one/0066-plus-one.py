class Solution(object):
    def plusOne(self, digits):
        s =int(''.join([str(i) for i in digits]))
        s = s + 1
        result = list(str(s))
        return [int(i) for i in result]
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        