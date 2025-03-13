public class App {
    /**
     * Computes the present value of a perpetuity.
     * 
     * @param C The initial cash flow of a perpetuity.
     * @param g The annual growth rate of the perpetuity.
     * @param r The discount rate of the perpetuity (cost of capital).
     * @param taxRate The annual tax rate.
     * @return The present value of the perpetuity.
     *
     * @throws IllegalArgumentException if C, g, or r are negative
     *     or when r <= g.
     */
    public static float getPresentValue(float C, float g, float r, float taxRate) {
        if (g >= r) {
            throw new IllegalArgumentException("Discount rate must be greater than growth rate");
        }
        if (C < 0 || g < 0 || r < 0 || taxRate < 0) {
            throw new IllegalArgumentException("Require non negative values");
        }
        if (r > 1.0f || taxRate > 1.0f) {
            throw new IllegalArgumentException("Unexpected discount rate and tax rate");
        }
        float year1 = C * (1 + g) * (1 - taxRate);
        return year1 / (r - g);
    }

    public static void main(String[] args) throws Exception {
        float C = 1000.f;
        float r = 0.1f;
        float g = 0.03f;
        float avg = getPresentValue(C, g, r, 0);
        System.out.println(avg);
    }
}
