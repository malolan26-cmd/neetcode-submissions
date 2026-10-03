class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            hashmap[num] = index

        print(hashmap)

        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashmap and index != hashmap[difference]:
                return [index, hashmap[difference]]