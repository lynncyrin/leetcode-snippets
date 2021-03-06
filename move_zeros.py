# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                nums[0 : len(nums)] = nums[0:i] + nums[i + 1 : len(nums)] + [0]
            else:
                i += 1
