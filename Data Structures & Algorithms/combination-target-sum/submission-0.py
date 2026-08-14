class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, current_subset, total):
            if total == target:
                res.append(current_subset.copy())
                return

            if index >= len(nums) or total > target:
                return

            current_subset.append(nums[index])
            dfs(index, current_subset, (total + nums[index]))
            current_subset.pop()
            dfs(index + 1, current_subset, total)
        
        dfs(0, [], 0)
        return res