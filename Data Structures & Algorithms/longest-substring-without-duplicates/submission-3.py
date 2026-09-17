class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):


            while s[r] in currSet:
                currSet.remove(s[l])
                l +=1

            currSet.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
