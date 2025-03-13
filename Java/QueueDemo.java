import java.util.LinkedList;
import java.util.Queue;

public class QueueDemo {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();

        // Adding elements to the Queue
        queue.add("John");
        queue.add("Jane");
        queue.add("Doe");

        System.out.println("Initial Queue: " + queue);

        // Removing an element
        String removedElement = queue.poll();
        System.out.println("Removed Element: " + removedElement);
        System.out.println("Queue after removal: " + queue);

        // Viewing the head of the queue without removal
        String headElement = queue.peek();
        System.out.println("Head of the Queue: " + headElement);
    }
}
