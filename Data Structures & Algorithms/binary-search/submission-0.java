class Solution {
    public int search(int[] nums, int target) {
        // Start with middle value

        // If middle value is lower, exclude it and take half again and go to next value to check. 

        // If middle value is higher, exclude and take remaining lower half and divide by 2 to check next value. 

        // Keep doing this process until value is found or cannot divide by 2, meaning not foundabstract

        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            
            int middle = left + (right - left) / 2;

            if (nums[middle] == target) {
                return middle;
            }

            if (nums[middle] > target) {
                right = middle - 1;

            } else {
                left = middle + 1;
            }
        }

        return -1;
    }
}
