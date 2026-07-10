class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # dictionary for count, values that occur 'count' number of times
        frequencies = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)
        
        for n, c in count.items():
            frequencies[c].append(n)
        print(frequencies)
        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for n in frequencies[i]:
                res.append(n)
                if len(res) == k:
                    return res

        