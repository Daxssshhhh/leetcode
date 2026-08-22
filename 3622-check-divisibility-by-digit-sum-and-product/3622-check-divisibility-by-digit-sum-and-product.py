class Solution(object):
    def checkDivisibility(self, n):
        temp = n
        summ = 0
        product = 1

        while temp > 0:
            digit = temp % 10
            summ += digit
            product *= digit
            temp = temp // 10

        return n % (summ + product) == 0