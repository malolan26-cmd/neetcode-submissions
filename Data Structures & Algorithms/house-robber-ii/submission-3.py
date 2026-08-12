class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_helper(nums):

            nums[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])

            return nums[-1]

        left = rob_helper(nums[:-1])
        right = rob_helper(nums[1:])

        return max(left, right)
        