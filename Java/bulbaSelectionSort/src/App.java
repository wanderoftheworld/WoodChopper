
public class App {
    /**
     * Computes average daily return.
     * 
     * @param prices The daily closing prices of a stock
     * @return The averay daily return when there are at least 2 elements in input;
     *     otherwise, 0 is returned.
     *
     * @throws IllegalArgumentException all elements in input must be a positive
     *     number; the last element can be 0.
     */
    public static float averageDailyReturn(float[] prices) {
        if (prices.length < 2) {
            return 0;
        }
    
        // The return on day i is defined as (price[i] - price[i-1]) / price[i-1].
        float sumOfReturn = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i - 1] <= 0 || prices[i] < 0) {
                throw new IllegalArgumentException("Price must be positive number");
            }
            sumOfReturn += (prices[i] - prices[i-1]) / prices[i-1];
        }
        return sumOfReturn / (prices.length - 1);
    }

    public static int evaluate(String expr) {
        int result = Character.getNumericValue(expr.charAt(0));

        for (int i = 1; i < expr.length(); i += 2) {
            char operator = expr.charAt(i);
            int operand = Character.getNumericValue(expr.charAt(i+1));

            switch (operator) {
                case '+':
                    result += operand;
                    break;
                case '-':
                    result -= operand;
                    break;
                case '*':
                    result *= operand;
                    break;
                default:
                    throw new IllegalArgumentException("BAA");
            }
        }
        return result;
    }

    public static void selectionSort(int[] array) {
        int n = array.length;
     
        for (int i = 0; i < n - 1; i++) {
            // Find the minimum element in unsorted subarray.
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (array[j] < array[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap the found minimum element with the first
            // element.
            int temp = array[minIdx];
            array[minIdx] = array[i];
            array[i] = temp;
        }
    }

    public static void main(String[] args) throws Exception {
        float[] prices = {1, 2, 6};
        float avg = averageDailyReturn(prices);
        System.out.println(avg);
        System.out.println(evaluate("3+5*7"));
        System.out.println(evaluate("4-8*9*1"));
        System.out.println(evaluate("0"));
        System.out.println(evaluate("1*2*3*4*5*6*7*8*9"));
    }
}
