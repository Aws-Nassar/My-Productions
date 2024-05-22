import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Interface	extends Remote 
{
	public double getADCost(int days) throws RemoteException;	
}