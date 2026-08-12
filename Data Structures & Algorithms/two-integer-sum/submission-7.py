class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexVal = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in indexVal:
                return [indexVal[diff], index]
            indexVal[num] = index
        return []