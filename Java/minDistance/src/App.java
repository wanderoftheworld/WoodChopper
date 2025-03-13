import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

public class App {
    public static void dfs(int nodeId, int[] seen, List<Integer> found,
            HashMap<Integer, HashSet<Integer>> adjMap) {
        seen[nodeId] = 1;
        HashSet<Integer> neighbors = adjMap.get(nodeId);
        if (neighbors != null) {
            found.add(nodeId);
            for (Integer n : neighbors) {
                if (seen[n] == 1) continue;
                dfs(n, seen, found, adjMap);
            }
        }
    }
    public static int minHammingDistance(int[] source, int[] target,
        List<int[]> allowedSwaps) {
        if (source.length != target.length) {
            throw new IllegalArgumentException(
                "'source' and 'target' must have the same number of elements.");
        }
        // Get the initial hamming distance.
        int distance = 0;
        for (int i = 0; i < source.length; i++) {
            if (source[i] != target[i]) {
                distance += 1;
            }
        }
        if (distance == 0 || source.length <= 1) {
            return distance;
        }
        distance = source.length;
        // Use a graph to identify groups of connected elements:
        // all elements connected via AllowedSwaps can be arranged
        // in any order.
        HashMap<Integer, HashSet<Integer>> adjacenMap = new HashMap<>();
        for (int i = 0; i < allowedSwaps.size(); i++) {
            int from = allowedSwaps.get(i)[0];
            int to = allowedSwaps.get(i)[1];
            if (from < 0 || to < 0 || from >= source.length || to >= source.length) {
                throw new IllegalArgumentException("Bad swap " + from + " to " + to);
            }
            if (adjacenMap.get(from) == null) {
                adjacenMap.put(from, new HashSet<Integer>());
            }
            adjacenMap.get(from).add(to);
            if (adjacenMap.get(to) == null) {
                adjacenMap.put(to, new HashSet<Integer>());
            }
            adjacenMap.get(to).add(from);
        }
        int[] seen = new int[source.length];
        for (int i = 0; i < source.length; i++) {
            if (seen[i] == 1) continue;
            List<Integer> found = new ArrayList<>();
            dfs(i, seen, found, adjacenMap);
            List<Integer> fromSource = new ArrayList<>();
            List<Integer> fromTarget = new ArrayList<>();
            for (int nodeId : found) {
                fromSource.add(source[nodeId]);
                fromTarget.add(target[nodeId]);
            }
            // Take the intersection.
            for (int num : fromSource) {
                if (fromTarget.contains(num)) {
                    fromTarget.remove(new Integer(num));
                    distance -= 1;
                }
            }
        }

        return distance;
    }
    
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
    }
}
