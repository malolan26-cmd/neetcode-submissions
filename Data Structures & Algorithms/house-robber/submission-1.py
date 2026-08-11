class Solution:
    def dfs(self, nums: List[int], cache) -> int:
        n = len(nums)
        if n in cache:
            return cache[n]

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # n >= 3
        res = max(self.dfs(nums[:n-2], cache)+nums[n-1], self.dfs(nums[:n-1], cache))
        cache[n] = res
        return res

    def rob(self, nums: List[int]) -> int:
        cache = {}

        return self.dfs(nums, cache)


        