import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ProductImpl extends UnicastRemoteObject implements Product {

    public ProductImpl() throws RemoteException {
        super();
    }

    @Override
    public int multiply(int a, int b) throws RemoteException {
        return a * b;
    }
}
