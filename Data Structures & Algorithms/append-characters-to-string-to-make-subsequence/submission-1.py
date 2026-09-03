class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_iterator = 0
        t_iterator = 0
        matching_count = 0

        while (s_iterator < len(s) and t_iterator < len(t)):
            if s[s_iterator] == t[t_iterator]:
                matching_count += 1
                t_iterator += 1
            s_iterator += 1

        if matching_count == len(t):
            return 0
        else:
            return len(t) - matching_count
