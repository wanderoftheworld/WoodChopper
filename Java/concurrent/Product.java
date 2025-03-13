import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Product extends Remote {
    int multiply(int a, int b) throws RemoteException;
}
