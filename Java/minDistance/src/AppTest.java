
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AppTest {
    @Test
    public void testIdenticalArrays() {
        int[] source = {1, 2, 3};
        int[] target = {1, 2, 3};
        int[] oneSwap = {1, 2};
        assertEquals(0, App.minHammingDistance(source, target, List.of()));
        assertEquals(0, App.minHammingDistance(source, target, List.of(oneSwap)));
    }
    @Test
    public void testSingleElementArrays() {
        int[] source = {5};
        int[] target = {6};
        int[] outOfBoundSwap = {1, 2};
        assertEquals(1, App.minHammingDistance(source, target, List.of()));
        assertEquals(1, App.minHammingDistance(source, target, List.of(outOfBoundSwap)));
    }
    @Test
    public void testDifferentArrays() {
        int[] source = {1, 2, 3};
        int[] target = {1, 3, 2};
        int[] oneSwap = {1, 2};
        int[] noopSwap = {0, 0};
        int[] outOfBoundSwap = {3, 2};
        int result = App.minHammingDistance(source, target, List.of(oneSwap, noopSwap));
        assertEquals(0, result);
        assertThrows(
            IllegalArgumentException.class,
            () -> App.minHammingDistance(source, target, List.of(outOfBoundSwap)));
    }
    @Test
    public void testMultipleSwapsDifferentPermutations() {
        int[] source = {1, 2, 3, 4};
        int[] target = {4, 3, 2, 1};
        int[] swapOne = {0, 3};
        int[] swapTwo = {1, 3};
        int[] swapThree = {2, 1};;
        // swapOne and swapThree are sufficient to get hamming distance to 0.
        int result = App.minHammingDistance(source, target, List.of(swapOne, swapThree));
        assertEquals(0, result);
        result = App.minHammingDistance(source, target, List.of(swapOne, swapTwo, swapThree));
        assertEquals(0, result);
    }
}
