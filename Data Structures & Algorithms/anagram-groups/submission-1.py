class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString not in res:
                res[sortedString] = []
            res[sortedString].append(string)

        return list(res.values())