class Solution {
    public int maxProfit(int[] prices) {
        // Checking if the current and the next are increasing is the key
        // If current is greater than next, make next the new current
        // With new current, check if the next is greater than current
        // Then check if next next is greater than next, so on until we find a max of the nexts
        // Return the difference if it drops off? 

        // Or check current with rest of array difference and find the max of those differencesabstract
        // If the value is positive, return it, if not return 0

        int maxDifference = 0;

        for (int i = 0; i < prices.length - 1; i++) {
            
            for (int j = i + 1; j < prices.length; j++) {

                if (prices[j] - prices[i] > maxDifference) {
                    maxDifference = prices[j] - prices[i];
                }
            }
        }
        if (maxDifference > 0) {
            return maxDifference;
        }
        return 0;
    }

}
