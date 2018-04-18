package security;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.util.Scanner;
import java.io.*;

public class Server {

	
	public static void main(String[] args) throws Exception{
		
		Socket ClientSocket = null;
		
		checkFiles();

		try{
			
			ServerSocket ss = new ServerSocket(9999);
			ss.setSoTimeout(10000);
			
			while (true){
				
				try{
					
					System.out.println("Waiting on :" + ss.getLocalPort());
					ClientSocket = ss.accept();
					System.out.println("Accepted Connection on: " +ClientSocket.getPort());
					new Client(ClientSocket);
					
					
					
				}
				catch(SocketTimeoutException ste){
					
					System.out.println("Timeout Occured: Trying again in 10000 seconds");
					Thread.sleep(1000);
				}
				
				
			}//connection established
			
		}
		catch(IOException ioe){
			
			System.out.print("Problem Occured Establishing A connection with port: " + 9999);
			
		}
		
	}//main method ends
		
	
	
	/****
	  Checks if the files (user and group) exists . if they do it just return , else it creates the files and then returns;
	 *****/

	public static void checkFiles() throws Exception{
	
		
		
		File user =  new File("/ilab/users/ims57/Desktop/security_project/user.txt");
		
		if (!user.exists()){
			
			user.createNewFile();
		}
		
		
		
		File groups = new File("/ilab/users/ims57/Desktop/security_project/groups.txt");
		
		if(!groups.exists()){
			
			groups.createNewFile();
		}
		
		return ;
		
		
	}	
	
} //class ends



