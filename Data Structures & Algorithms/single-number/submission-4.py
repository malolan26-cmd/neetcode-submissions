class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        print(nums)
        while True:
            if i >= len(nums) - 1:
                return nums[-1]
            elif nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
            
        
        
