import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ProductInterface extends Remote {
    int getProduct(int a, int b) throws RemoteException;
}
