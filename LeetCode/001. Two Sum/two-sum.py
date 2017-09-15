class Solution:
    def twoSum(self, nums, target):
        """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        Args:
            nums: An array of integers
            target: A specific target integer of which can be summed to by two elements within the nums array

        Return:
            An array of size two containing the indices of the two numbers such that they add up to a specific target
        """
        idxs = {nums[idx]: idx for idx in range(len(nums))}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in idxs and idxs[new_target] != i:
                return [i, idxs[new_target]]
