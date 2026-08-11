class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        num_steps = [0] * (n + 1)
        num_steps[1], num_steps[2] = 1, 2

        for i in range(3, n + 1):
            num_steps[i] = num_steps[i - 1] + num_steps[i - 2]

        return num_steps[n]