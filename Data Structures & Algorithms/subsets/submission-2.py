class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_subset = []

        def dfs(index):
            if index >= len(nums):
                res.append(current_subset.copy())
                return
            
            current_subset.append(nums[index])
            dfs(index + 1)
            current_subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return res

