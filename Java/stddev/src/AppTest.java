import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AppTest {

    @Test
    public void testZeroTaxRate() {
        float expectedPV = 14714.286f;
        float pv = App.getPresentValue(1000.f, 0.03f, 0.1f, 0);
        assertEquals(expectedPV, pv);
    }

    @Test
    public void testNormal() {
        float expectedPV = 13242.857f;
        float pv = App.getPresentValue(1000.f, 0.03f, 0.1f, 0.1f);
        assertEquals(expectedPV, pv);       
    }
    
    @Test
    public void testZeroInitialCash() {
        float pv = App.getPresentValue(0, 0.03f, 0.1f, 0.1f);
        assertEquals(0, pv);
    }

    @Test
    public void testInvalidInput() {
        assertThrows(
           IllegalArgumentException.class,
           () -> App.getPresentValue(-1000.f, 0.03f, 0.1f, 0));
        assertThrows(
            IllegalArgumentException.class,
            () -> App.getPresentValue(1000.f, 0.1f, 0.03f, 0));
        assertThrows(
            IllegalArgumentException.class,
            () -> App.getPresentValue(1000.f, 0.1f, 0.03f, 1.0f));
    }
}

