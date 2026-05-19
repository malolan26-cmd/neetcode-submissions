class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().trim();


        // Googled this
        s = s.replaceAll("[^a-zA-Z0-9]", "");

        int rightIndex = s.length() - 1;
        int leftIndex = 0;

        // Check from left and right and make sure that the values match
        while (leftIndex < rightIndex) {
            if (s.charAt(leftIndex) != s.charAt(rightIndex)) {
                return false;
            }

            leftIndex++;
            rightIndex--;
        }
        return true;
    }
}
