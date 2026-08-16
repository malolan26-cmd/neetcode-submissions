class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        i = 1
        while True:
            for j in range(i,2*i):
                if j > n:
                    return res
                res[j] = res[j - i] + 1
            i = i * 2