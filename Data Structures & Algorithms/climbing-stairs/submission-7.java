
class Solution {
    public int climbStairs(int n) {
        int[] cache = new int[46];
        for (int i = 1; i <= 45; i++) {
            cache[i] = -1;
        }
        cache[0] = 0;
        cache[1] = 1;
        cache[2] = 2;
        cache[3] = 3;

        return helperClimbStairs(n, cache);

        
    }

    public int helperClimbStairs(int n, int[] cache) {
        if (cache[n] > -1) {
            return cache[n];
        }
        
        int result = helperClimbStairs(n - 1, cache) + helperClimbStairs(n - 2, cache);
        
        cache[n] = result;

        return result;
        
    }

    
}
