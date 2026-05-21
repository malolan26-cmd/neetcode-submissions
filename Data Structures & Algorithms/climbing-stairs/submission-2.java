
class Solution {
    public int climbStairs(int n) {
        Hashtable<Integer, Integer> cache = new Hashtable<>();

        return helperClimbStairs(n, cache);

        
    }

    public int helperClimbStairs(int n, Hashtable<Integer, Integer> cache) {
        if (cache.containsKey(n)) {
            return cache.get(n);
        }
        
        if (n == 0) {
            cache.put(0, 0);
            return 0;
        }
        if (n == 1) {
            cache.put(1,1);
            return 1;
        }
        if (n == 2) {
            cache.put(2,2);
            return 2;
        }
        int result = helperClimbStairs(n - 1, cache) + helperClimbStairs(n - 2, cache);
        
        cache.put(n, result);

        return result;
        
    }

    
}
