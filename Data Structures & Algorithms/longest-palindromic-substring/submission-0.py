class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_length = 0

        for i in range(len(s)):
            l, r = i, i
            
            # Odd length string, using one value as center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res_length = r - l + 1
                    res = s[l:r+1]
                
                l -= 1
                r += 1

            l, r = i, i + 1
            # Even length string, compare two values to start
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res_length = r - l + 1
                    res = s[l:r+1]
                
                l -= 1
                r += 1

        return res
            

        