import java.util.Scanner;

public class MeltingIce {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int i = 0; i < T; i++) {
            long E = scanner.nextLong(); // Use long to handle larger values of E
            long K = scanner.nextLong();

            int friendsNeeded = calculateFriendsNeeded(E, K);
            System.out.println(friendsNeeded + 1); // Add 1 for Ukesh
        }
        scanner.close();
    }

    public static int calculateFriendsNeeded(long E, long K) {
        if (E <= K) {
            return 1; // Ice melts completely in one round
        }
        int friends = 0;
        while (E > K) {
            E = (E + K - 1) / K; // Efficiently calculate floor(E / K) using integer division
            friends++;
        }
        return friends;
    }
}
