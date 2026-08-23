class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # If number of ? is odd, Alice always wins
        if (left_q + right_q) % 2 == 1:
            return True

        # Difference in number of ? between two halves
        q_diff = left_q - right_q

        # Maximum difference that can be compensated
        sum_diff = left_sum - right_sum

        return sum_diff != -q_diff * 9 // 2