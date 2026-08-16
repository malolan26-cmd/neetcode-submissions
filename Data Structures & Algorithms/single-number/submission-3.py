class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if flag is still true by the end of the loop iteration, return the current element
        for i in range(len(nums)):
            flag = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    flag = False
            if flag:
                return nums[i]
