import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class client 
{
	public static void main(String []args) 
    {
        boolean flag = true;
        while (flag)
        {
            try
            {
                System.out.println("\n******* Main Menu *******\n");
                System.out.println("1. Calculate the AD cost.");
                System.out.println("2. Exit.");
                System.out.print("--> ");
                Scanner input = new Scanner(System.in);
                int option = input.nextInt();
                if (option == 1)
                {
                    System.out.println("\n======\n");
                    try
                    {
                        Registry registry = LocateRegistry.getRegistry("localhost", 2001);
                        System.out.print("Enter number of days: ");
                        Scanner in = new Scanner(System.in);
                        int days = in.nextInt();
                        if(days <= 10)
                        {
                            Interface stub = (Interface)registry.lookup("server1");
                            System.out.println("The AD cost for " + days + " days = " + stub.getADCost(days));
                        }
                        else 
                        {
                            Interface stub = (Interface)registry.lookup("server2");
                            System.out.println("The AD cost for " + days + " days = " + stub.getADCost(days));
                        }
                    }
                    catch (Exception e) 
                    {
                        System.err.println("Client exception: " + e.toString());
                        e.printStackTrace();
                    }
                    System.out.println("\n\n--------------------------------------\n\n");
                }
                else if(option == 2)
                {
                    System.out.println("\n*********\nSalamat\n*********\n");
                    flag = false;
                }
            }
            catch (Exception e)
            { 
                e.printStackTrace();  
            } 
        }
  	}
}

