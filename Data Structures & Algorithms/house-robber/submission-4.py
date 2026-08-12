class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums) - 1

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        max_index_minus_one = max(nums[0], nums[1])
        max_index_minus_two = nums[0]

        for num in nums[2:]:
            max_index_minus_two, max_index_minus_one = (
                max_index_minus_one, max(num + max_index_minus_two, max_index_minus_one)
            )
        print(max_index_minus_one, max_index_minus_two)
        return max_index_minus_one