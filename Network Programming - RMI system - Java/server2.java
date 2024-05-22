import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;	

public class server2 implements Interface
{
	public server2() throws RemoteException
	{
		System.out.println("Creating server2 Object");
	}

	public double getADCost(int days) throws RemoteException
	{
		System.err.println("the client sent :" + days + " days");
		return (days * 10) - (days * 0.05);
	}
	
	public static void main(String []args) 
	{
		try 
		{
            server2 serverObject2 = new server2();
            Interface skelton = (Interface) UnicastRemoteObject.exportObject(serverObject2, 0);
            Registry registry = LocateRegistry.getRegistry(2001);
            registry.bind("server2", skelton);
			System.out.println("Server2 ready");
        } 
		catch (Exception e)
		{
			System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
 	}
}
