import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;	

public class server1 implements Interface
{
	public server1() throws RemoteException
	{
		System.out.println("Creating server1 Object");
	}

	public double getADCost(int days) throws RemoteException
	{
		System.err.println("the client sent :" + days + " days");
		return days * 10;
	}
	
	public static void main(String []args) {
		try 
		{
            server1 serverObject1 = new server1();
            Interface skelton = (Interface) UnicastRemoteObject.exportObject(serverObject1, 0);
            Registry registry = LocateRegistry.getRegistry(2001);
            registry.bind("server1", skelton);
			System.out.println("Server1 ready");
        } 
		catch (Exception e)
		{
			System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
 	}
}
