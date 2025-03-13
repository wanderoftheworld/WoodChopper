import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        Queue<String> myQueue = new LinkedList<>();

        // Adding elements:
        myQueue.add("Element 1");
        myQueue.offer("Element 2"); 

        // Accessing/removing elements:
        System.out.println("Head of queue: " + myQueue.peek()); 
        System.out.println("Removed element: " + myQueue.remove());
    }
}
