class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 0

        curr_num = nums[0]
        longest_streak = 0

        i = 0

        while i < len(nums):
            if curr_num != nums[i]:
                curr_num = nums[i]
                longest_streak = 0
            while i < len(nums) and nums[i] == curr_num:
                i += 1
            longest_streak += 1
            curr_num += 1
            res = max(res, longest_streak)

        return res

        