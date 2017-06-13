class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        current_ones = 0
        for i in nums:
            if i == 1:
                current_ones += 1
            else:
                current_ones = 0
            if current_ones > max_ones:
                max_ones = current_ones
        return max_ones
