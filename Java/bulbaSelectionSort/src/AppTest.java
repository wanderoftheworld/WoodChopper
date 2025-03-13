import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AppTest {

    @Test
    public void testNotEnoughPrices() {
        float[] zeroPrices = {};
        float[] onlyOnePrice = {1.f};
        float expectedAvgReturn = 0;
        float avgReturn = App.averageDailyReturn(zeroPrices);
        assertEquals(expectedAvgReturn, avgReturn);
        avgReturn = App.averageDailyReturn(onlyOnePrice);
        assertEquals(expectedAvgReturn, avgReturn);
    }

    @Test
    public void testNormal() {
        float[] array = {2, 4, 3};
        float expectedAvgReturn = 0.375f;
        float avgReturn = App.averageDailyReturn(array);
        assertEquals(expectedAvgReturn, avgReturn);
    }

    @Test
    public void testSamePriceEveryday() {
        float[] array = {2, 2, 2, 2};
        float expectedAvgReturn = 0;
        float avgReturn = App.averageDailyReturn(array);
        assertEquals(expectedAvgReturn, avgReturn);       
    }
    
    @Test
    public void testZeroPriceAtEnd() {
        float[] array = {2, 4, 0};
        float expectedAvgReturn = 0;
        float avgReturn = App.averageDailyReturn(array);
        assertEquals(expectedAvgReturn, avgReturn);
    }

    @Test
    public void testInvalidPrice() {
        float[] array1 = {-2, 4, 0};
        float[] array2 = {0, 1, 2};
        assertThrows(
           IllegalArgumentException.class,
           () -> App.averageDailyReturn(array1));
        assertThrows(
            IllegalArgumentException.class,
            () -> App.averageDailyReturn(array2));
    }
}

