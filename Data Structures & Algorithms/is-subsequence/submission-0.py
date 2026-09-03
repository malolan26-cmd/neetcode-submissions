class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_iterator = 0
        t_iterator = 0

        while (s_iterator < len(s) and t_iterator < len(t)):
            if (s[s_iterator] == t[t_iterator]):
                s_iterator += 1
            
            t_iterator += 1

        return s_iterator == len(s)