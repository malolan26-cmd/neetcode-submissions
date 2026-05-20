class Solution {
    public boolean isHappy(int n) {
        int sumOfSquares = digitsSquared(n);
        HashSet<Integer> seenNums = new HashSet<>();

        while (sumOfSquares != 1) {


            

            if (seenNums.add(sumOfSquares) != true) {
                return false;
            }

            sumOfSquares = digitsSquared(sumOfSquares);


        }
        return true;
    }

    public int digitsSquared(int n) {
        int sum = 0;
        String num = Integer.toString(n);
        char[] digitsAsChars = num.toCharArray();

        for (char digit : digitsAsChars) {
            int numDigit = Character.getNumericValue(digit);
            sum += numDigit * numDigit;
        }
        return sum;
    }
}
