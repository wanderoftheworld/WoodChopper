import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class ProductServer {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(10099);
            ProductImpl product = new ProductImpl();
            Naming.rebind("rmi://localhost:10099/ProductService", product);
            System.out.println("Server started...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
